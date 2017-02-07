DashboardHeader = '1520_DashboardHeaderSonar.png'
SonarArray = '48095_SonarArray.png'
SonarFunctions = '20100_SonarFunctions.png'
SonarFunctionsInfo = '65155_SonarFunctionInfo.png' 
sonarDiagHeader = '25315_sonarDiagHeader.png'
sonarDiagInfo = '65365_sonarDiagInfo.png'
SonarBottomHeader = '15520_SonarBottomHeader.png'
ForwardButton = '349183_ForwardButton.png'
RearButton = '350215_RearButton.png'
StartButton = '352396_StartButton.png'



import pygame
import os
from pygame.locals import *
pygame.init()

fullArrayReading=[]
forwardArrayReading=[]
rearArrayReading=[]
singleSonarReading=[]

myfont = pygame.font.SysFont("calibri",24)
screen = pygame.display.set_mode((966,550),0,32)

def renderSonarDash():
    
    screen = pygame.display.set_mode((966,550),0,32)
    pygame.display.set_caption("Robot User Interface")
    screen.fill((0,0,0))  
    myfont = pygame.font.SysFont("calibri",24)

    DashboardHeader = '1520_DashboardHeaderSonar.png'
    SonarArray = '48095_SonarArray.png'
    SonarFunctions = '20100_SonarFunctions.png'
    SonarFunctionsInfo = '65155_SonarFunctionInfo.png' 
    sonarDiagHeader = '25315_sonarDiagHeader.png'
    sonarDiagInfo = '65365_sonarDiagInfo.png'
    SonarBottomHeader = '15520_SonarBottomHeader.png'
    FullArrayButton = '350249_FullArrayButton.png'
    StartButton = '352396_StartButton.png'
    
                                

    DashboardHeader = pygame.image.load(os.path.join("Images",DashboardHeader))
    screen.blit(DashboardHeader,(15,20))
    SonarArray = pygame.image.load(os.path.join("Images",SonarArray))
    screen.blit(SonarArray,(480,95))
    SonarFunctions = pygame.image.load(os.path.join("Images",SonarFunctions))
    screen.blit(SonarFunctions,(20,100))
    SonarFunctionsInfo = pygame.image.load(os.path.join("Images",SonarFunctionsInfo))
    screen.blit(SonarFunctionsInfo,(65,155))
    sonarDiagHeader = pygame.image.load(os.path.join("Images",sonarDiagHeader))
    screen.blit(sonarDiagHeader,(25,315))
    sonarDiagInfo = pygame.image.load(os.path.join("Images",sonarDiagInfo))
    screen.blit(sonarDiagInfo,(65,365))
    SonarBottomHeader = pygame.image.load(os.path.join("Images",SonarBottomHeader))
    screen.blit(SonarBottomHeader,(15,520))
    StartButton = pygame.image.load(os.path.join("Images",StartButton))
    screen.blit(StartButton,(352,396))
    return

def convertArrayToStringList(arrayValues):

    for index in range(len(arrayValues)):
        arrayValues[index]=(str(arrayValues[index]))
        arrayValues[index]=''.join((arrayValues[index],"cm"))    
    print(arrayValues)
    return arrayValues

def displayFullArrayValues(fullArrayReading):
    SA1 = myfont.render(fullArrayReading[0],1,(255,255,255)) 
    screen.blit(SA1,(890,177))
    SA2 = myfont.render(fullArrayReading[1],1,(255,255,255)) 
    screen.blit(SA2,(890,218))                
    SA3 = myfont.render(fullArrayReading[2],1,(255,255,255)) 
    screen.blit(SA3,(890,312))
    SA4 = myfont.render(fullArrayReading[3],1,(255,255,255)) 
    screen.blit(SA4,(890,402))
    SA5 = myfont.render(fullArrayReading[4],1,(255,255,255)) 
    screen.blit(SA5,(890,450))
    SA6 = myfont.render(fullArrayReading[5],1,(255,255,255)) 
    screen.blit(SA6,(890,490))
    SA7 = myfont.render(fullArrayReading[6],1,(255,255,255)) 
    screen.blit(SA7,(495,450))
    SA8 = myfont.render(fullArrayReading[7],1,(255,255,255)) 
    screen.blit(SA8,(495,402))
    SA9 = myfont.render(fullArrayReading[8],1,(255,255,255)) 
    screen.blit(SA9,(495,312))
    SA10 = myfont.render(fullArrayReading[9],1,(255,255,255)) 
    screen.blit(SA10,(495,218))
    SA11 = myfont.render(fullArrayReading[10],1,(255,255,255)) 
    screen.blit(SA11,(495,177))
    SA12 = myfont.render(fullArrayReading[11],1,(255,255,255)) 
    screen.blit(SA12,(495,135))    
    return

def displayForwardArrayValues(forwardArray):
    SA1 = myfont.render(forwardArray[2],1,(255,255,255)) 
    screen.blit(SA1,(890,177))
    SA11 = myfont.render(forwardArray[0],1,(255,255,255)) 
    screen.blit(SA11,(495,177))
    SA12 = myfont.render(forwardArray[1],1,(255,255,255)) 
    screen.blit(SA12,(495,135))    
    return

def displayRearArrayValues(rearArray):
    SA5 = myfont.render(rearArray[0],1,(255,255,255)) 
    screen.blit(SA5,(890,450))
    SA6 = myfont.render(rearArray[1],1,(255,255,255)) 
    screen.blit(SA6,(890,490))
    SA7 = myfont.render(rearArray[2],1,(255,255,255)) 
    screen.blit(SA7,(495,450))

    return
    
def sonarFailure(sonarNumberFailed):
    print('_SonarDashboard_Functions.sonarFailure() Entered')
    SonarError = 'error.png'
    SonarError = pygame.image.load(os.path.join("Images",SonarError))
    if sonarNumberFailed[1] == '0x01':
        screen.blit(SonarError,(890,177))
    if sonarNumberFailed[1] == '0x02':
        screen.blit(SonarError,(890,218))
    if sonarNumberFailed[1] == '0x03':
        screen.blit(SonarError,(890,312))
    if sonarNumberFailed[1] == '0x04':
        screen.blit(SonarError,(890,402))
    if sonarNumberFailed[1] == '0x05':
        screen.blit(SonarError,(890,450))
    if sonarNumberFailed[1] == '0x06':
        screen.blit(SonarError,(890,490))
    if sonarNumberFailed[1] == '0x07':
        screen.blit(SonarError,(505,450))
    if sonarNumberFailed[1] == '0x08':
        print('_SonarDashboard_Functions.sonarFailure() Failed Sensor 8')
        screen.blit(SonarError,(505,402))
    if sonarNumberFailed[1] == '0x09':
        screen.blit(SonarError,(505,312))
    if sonarNumberFailed[1] == '0x10':
        screen.blit(SonarError,(505,218))
    if sonarNumberFailed[1] == '0x11':
        screen.blit(SonarError,(505,177))
    if sonarNumberFailed[1] == '0x12':
        screen.blit(SonarError,(505,135))
    return

        
    
    
