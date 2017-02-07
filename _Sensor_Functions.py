#Modue - Sensor Functions
#Defines functions required for communication to sensor module
#R.McQueen
#robertjmcqueen@googlemail.com

import serial
import time

serSensor = serial.Serial(port='/dev/ttyACM0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)



#Servo control varialble
solonoidPos=0
hzPos=0
vtPos=0
servoSpeed=0

#Tx messages
startDiagnosticSession=bytes([0x10])
sleepMode=bytes([0x11])
fullSensorArrayReading=bytes([0x33])
readForwardArray=bytes([0x42])
readRearArray=bytes([0x43])
activateSolonoid=bytes([0x50])
deactivateSolonoid=bytes([0x51])
wakeUp=bytes([0xFF])
controlServoPosition=bytes([0xA0,hzPos,vtPos,servoSpeed])

#RxMessages
FailedDiagnosticSession = '0x12'
PassedDiagnsoticSession = '0x11'
RecievedFullArrayReading = '0x66'


#initalise global variables
line=[]
SonarSensorArray=[]
readingList=[]
DiagnosticResult=0x00

#*************************************************************
#Low level Functions
#*************************************************************


def captureSonarArray(arraySize):
    global SonarSensorArray
    global readingList
    x=0
    bComplete=False
    readingList=[]
    SonarSensorArray =[]
    while bComplete==False:                          #Value set to set a maximum number of bytes in the buffer array comming back from the Arduino
        for c in serSensor.read():                      #start reading the buffer
            if c!=10:                                   #filter end of line chars
                if c!=13:                               #filter end of line chars
                    SonarSensorArray.append(c)          #Append the SonarSensor array with a read distance value
                 
            else:
                reading= map(chr,SonarSensorArray)      #MAp the car into a reading buffer
                reading=''.join(reading)                #Add it to the reading buffer
                #print(reading)                          #Print the reading value
                if reading != '':
                    reading=(int(reading))
                    readingList.append(reading)
                    if arraySize==len(readingList):
                        bComplete=True
                        break
                SonarSensorArray =[]
    
    print('The Length of reading list is, ',len(readingList))
    print(readingList)
    SonarSensorArray=[]
    return True
    
def readMessage(arraySize):
    messageRecieved=False
    bResult=False
    global line 
    while messageRecieved==False:
        for b in serSensor.read():
            b=format(b,'#04x')
            line.append(b)                              #convert from ASCI 
            if b=='0x0a':                               #End of Message detected for diagnsotics and sleep
                print(line)                             #Print the message buffer
                #messageRecieved = decodeMessage(line)   #DecodeMessage
                if line[0]==FailedDiagnosticSession:
                    #DiagnosticResult=line[0]
                    print("_Sensor_Functions.decodeMessage.... Result failed 0x12 Sensor number",line[1])
                    messageRecieved= True
                    bResult=False
                if line[0]==PassedDiagnsoticSession:
                    #DiagnosticResult=line[0]
                    print("_Sensor_Functions.decodeMessage.... Result Passed 0x11")
                    messageRecieved= True
                    bResult=True
                else:
                    messageRecieved=False              
                line=[]                                 #clear the buffer
            if b=='0x66':                               #This is the positive response for a sonar array message
                messageRecieved=captureSonarArray(arraySize)     #Populate the messageREcieved buffer with sonar array
                line=[]                                 #clear the buffer
                bResult=messageRecieved
            time.sleep(0.1)
    return bResult

def sendSerialMessageSensorModule(message):
    print("_Sensor_Functions.sendSerialMessage.... - sendSerialMessageSensorModule() Entered ",message[0])
    serSensor.write(message)
    return


#*************************************************************
#Define API layer 
#*************************************************************

def executeDiagnostics():
    print("_Sensor_Functions.exectuteDiagnostics().... Entered")
    arraySize=12
    sendSerialMessageSensorModule(startDiagnosticSession)
    readMessage(arraySize)
    return

def getFullArrayReading():
    bResult = False
    print("_Sensor_Functions.getFullArrayReading().... Entered")
    arraySize=12
    sendSerialMessageSensorModule(fullSensorArrayReading)
    bResult=readMessage(arraySize)
    if bResult==True:
        #print(readingList)
        return readingList
    return

def monitorForwardArray():
    print("_Sensor_Functions.monitorForwardArray().... Entered")
    bResult = False
    arraySize=3
    sendSerialMessageSensorModule(readForwardArray)
    bResult=readMessage(arraySize)
    if bResult==True:
        #print(readingList)
        return readingList
    return

def monitorRearArray():
    print("_Sensor_Functions.monitorForwardArray().... Entered")
    bResult = False
    arraySize=3
    sendSerialMessageSensorModule(readRearArray)
    bResult=readMessage(arraySize)
    if bResult==True:
        #print(readingList)
        return readingList
    return

def sleepSensorModule():
    print("_Sensor_Functions.sleepSensorModule().... Entered")
    sendSerialMessageSensorModule(sleepMode)
    return







