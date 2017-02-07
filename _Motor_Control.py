#Module - Motor Control Software
#Defines Control sytem for the drive motors UART interface built into each motor.
#R.McQueen
#robertjmcqueen@googlemail.com


#Terminal No. Terminal Name Wire Color Description
#Terminal 1     GND             BLACK   Ground should be connected to negative of supply of battery
#Terminal 2 SCL/PPM/Analog      BROWN   I2C clock / PPM input signal / Analog Voltage Input
#Terminal 3 SDA/Analog Sense    RED     I2C Data / Analog Input Sense
#Terminal 4 UART TXD            ORANGE  UART Data Transmit of speed controller, connect to RXD of host
#Terminal 5 UART RXD            YELLOW  UART Data Receive of speed controller, connect to TXD of host
#Terminal 6 V+                  GREEN   V+ should be connected to positive of supply or battery


#Command                    Description                          Value Minimum           Value Maximum
motorSpeed = 'S'            #Read/Write Motor Speed and Direction    -255                    +255
motorMaxSpeed = 'M'         #Read/Write Motor Max Speed                0                      255
speedDamping ='D'           #Read/Write Speed Damping                  0                      255
loadDefaultValues = 'Y'     #Load Default Values of all settings and gains -                   -
encoderPosition = 'P'       #Read/Write Encoder Position          -2147483648              2147483647
gotoPosition = 'G'          #Read/Write Go to Position Command    -2147483648              2147483647
gotoRelativePosition = 'R'  #Write Relative Go to Position Command -2147483648             2147483647
#'A'                        #Read/Write Speed-Feedback Gain term       0                      32767
#'B'                        #Read/Write P-Gain term                    0                      32767
#'C'                        #Read/Write I-Gain term                    0                      32767
#'X'                        #Auto-calibrate Speed-Feedback Gain term   -                        -
#'E'                        #Read/Write I2C address                    0                      127

#NOTE: at 0.2 degrees resolution and wheel diameter of 63.5mm. 90 encoder positions = 1cm.

#import libraries
import serial
import time
import os

motorLH = serial.Serial(port='/dev/ttyUSB0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)


motorRH = serial.Serial(port='/dev/ttyUSB1',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)




#Define messages for all control messages. 


#Define Global Vars
_lhEncodePosition=0    #Left hand motor encoder position
_rhEncodePosition=0    #Right hand motor encoder position
byteArrayEL=13         #End of line 

#*************************************************************
#Low level functions
#*************************************************************


def writeMotorCommandLH(command,value):
    byteCommand=convert_str_to_byte_array(command+str(value))
    motorLH.write(bytes(byteCommand))
    #motorLH.write(bytes(byteArrayEL))
    x=motorLH.readline()
    print(x) 
    return

def writeMotorCommandRH(command,value):
    byteCommand=convert_str_to_byte_array(command+str(value))
    motorRH.write(bytes(byteCommand))
    return

def readMotorMessageLH(command):
    count=0
    byteCommand=convert_str_to_byte_array(command)
    motorLH.write(bytes(byteCommand))
    x=motorLH.readline()
    print(x)
    return x

def readMotorMessageRH(command):
    byteCommand=convert_str_to_byte_array(command)
    motorRH.write(bytes(byteCommand))
    while(count<10):
        x=motorRH.readline()
        print(x)
    return x

                 
# Returns the number of encoder positions required distance is in CM.
def calculateEncoderPositions(distance):
    return distance*9

def setMotorSpeeds(lhSpeed,RhSpeed):
    writeMotorCommandLH(motorMaxSpeed,lhSpeed)
    writeMotorCommandRH(motorMaxSpeed,RhSpeed)
    return

def convert_str_to_byte_array(sString):
    byteCommand = []                        #Create an empty list
    for ch in sString:                      #for every char in the string
        code = ord(ch)                      #convert to ascci int
        byteCommand.append(code)            #Add to the list
    byteCommand.append(byteArrayEL)         #Stick a carrage return on the end
    byteCommand =bytes(byteCommand)         #Convert final list to byte array
    return byteCommand                      #Return Byte array

def resetEncoderPositions():
    writeMotorCommandLH(encoderPosition,0)
    writeMotorCommandRH(encoderPosition,0)
    return

def prepareForDrive(distance,speed):
    resetEncoderPositions()                                 #Always reset encoder positions to 0
    encoderClicks = 0
    setMotorSpeeds(speed,speed)                             #Set motor speeds
    encoderClicks = calculateEncoderPositions(distance)     #Calcualte how many encoder positions to travel
    return encoderClicks

#*************************************************************
#API Layer
#*************************************************************



def Drive(distance,speed):  #Drive a given distance either + forward or -backwards
    encoderClicks=prepareForDrive(distance,speed)
    writeMotorCommandLH(gotoPosition,encoderClicks)         #Drive LH motor to required position
    writeMotorCommandRH(gotoPosition,encoderClicks)         #Drive RH motor to required position
    return

def RotateAngle(angle,direction,speed):
    encoderClicks=prepareForDrive(angle,speed)
    if(direction=='LT'):                                    #LT So drive RH motor
        writeMotorCommandRH(gotoPosition,encoderClicks)         #Drive RH motor to required position

    if(direction=='RT'):                                    #RT So drive LH motor
        writeMotorCommandLH(gotoPosition,encoderClicks)         #Drive RH motor to required position
        
    return

   
#*************************************************************
#Test Sequence
#*************************************************************

def testSequence1():
    writeMotorCommandLH(motorMaxSpeed,255)
    count=0
    iterations=0
    while(iterations<3):    
        while(count<255):
            writeMotorCommandLH(motorSpeed,count)
            count=count+5
        while(count>10):
            writeMotorCommandLH(motorSpeed,count)
            count=count-5
        iterations=iterations+1
    writeMotorCommandLH(motorSpeed,0)
    return

testSequence1()

