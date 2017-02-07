DashboardHeader = '1520_DashboardHeader.png'
ControlHeader = '35160_ControlHeader.png'
ControlButton = '300212_ControlButton.png'
NavigationButton = '300244_NAvigationButton.png' 
SonarButton = '400144_SonarButton.png'
DriveButton = '400177_DriveButton.png'
CameraButton = '400195_CameraButton.png'
WeaponButton = '400222_WeaponButton.png'
ActuatorButton = '400248_Actuation.png'
ExitButton = '300353_Exit.png'
Seperater = '300290_Seperator.png'

import pygame
import _Sensor_Functions
from pygame.locals import *
from sys import exit


fullArrayReading=[]
forwardArrayReading=[]
rearArrayReading=[]
singleSonarReading=[]



pygame.init()

screen = pygame.display.set_mode((966,550),0,32)
pygame.display.set_caption("Robot User Interface")

screen.fill((0,0,0))  


DashboardHeader = pygame.image.load(DashboardHeader)
screen.blit(DashboardHeader,(15,20))
ControlHeader = pygame.image.load(ControlHeader)
screen.blit(ControlHeader,(35,160))
ControlButton = pygame.image.load(ControlButton)
b=screen.blit(ControlButton,(300,212))
NavigationButton = pygame.image.load(NavigationButton)
screen.blit(NavigationButton,(300,244))
SonarButton = pygame.image.load(SonarButton)
screen.blit(SonarButton,(400,144))
DriveButton = pygame.image.load(DriveButton)
screen.blit(DriveButton,(400,171))
CameraButton = pygame.image.load(CameraButton)
screen.blit(CameraButton,(400,195))
WeaponButton = pygame.image.load(WeaponButton)
screen.blit(WeaponButton,(400,222))
ActuatorButton = pygame.image.load(ActuatorButton)
screen.blit(ActuatorButton,(400,248))
ExitButton = pygame.image.load(ExitButton)
screen.blit(ExitButton,(300,353))
Seperater = pygame.image.load(Seperater)
screen.blit(Seperater,(300,290))


def convertArrayToStringList(arrayValues):

    for index in range(len(arrayValues)):
        arrayValues[index]=(str(arrayValues[index]))
        arrayValues[index]=''.join((arrayValues[index],"cm"))
        
        
        
    print(arrayValues)




while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y =event.pos
            if b.collidepoint(x,y):
                print('Control Buton pressed')
                fullArrayReading=_Sensor_Functions.getFullArrayReading()
                print(fullArrayReading)
                convertArrayToStringList(fullArrayReading)
                
                
            
     
    
    pygame.display.update()




    


        
    
    
