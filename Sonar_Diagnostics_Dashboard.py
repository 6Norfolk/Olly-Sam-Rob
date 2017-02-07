FullArrayButton = '350249_FullArrayButton.png'
ForwardButton = '349183_ForwardButton.png'
RearButton = '350215_RearButton.png'
FullArrayButtonOn = '350249_FullArrayButtonOn.png'
ForwardButtonOn = '349183_ForwardButtonOn.png'
RearButtonOn = '350215_RearButtonOn.png'

import pygame
import os
import _Sensor_Functions
import _Sonar_Dashboard_Functions
from pygame.locals import *
from sys import exit
from time import sleep


FailedDiagnosticSession = '0x12'

fullArrayReading=[]
forwardArrayReading=[]
rearArrayReading=[]
singleSonarReading=[]

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

screen = pygame.display.set_mode((966,550),0,32)
_Sonar_Dashboard_Functions.renderSonarDash()
FullArrayButton = pygame.image.load(os.path.join("Images",FullArrayButton))
fa_clk=screen.blit(FullArrayButton,(350,249))
ForwardButton = pygame.image.load(os.path.join("Images",ForwardButton))
fb_clk = screen.blit(ForwardButton,(349,183))
RearButton = pygame.image.load(os.path.join("Images",RearButton))
rb_clk = screen.blit(RearButton,(350,215))

FullArrayButtonOn = pygame.image.load(os.path.join("Images",FullArrayButtonOn))
ForwardButtonOn = pygame.image.load(os.path.join("Images",ForwardButtonOn))
RearButtonOn = pygame.image.load(os.path.join("Images",RearButtonOn))

FullArrayButtonStatus =False

pygame.mixer.music.load("hailbeep.mp3")

def renderButtons():
    screen.blit(FullArrayButton,(350,249))
    screen.blit(ForwardButton,(349,183))
    screen.blit(RearButton,(350,215))
    return

def checkButtonStatus(button):
    if button == False:
        return True
    if button == True:
        return False
    
def pollFullArray():
    FullArrayButtonStatus = checkButtonStatus(FullArrayButtonStatus)
    if FullArrayButtonStatus == True:
        screen.blit(FullArrayButtonOn,(350,249))
        pygame.display.update()
        pygame.mixer.music.play()

    while FullArrayButtonStatus==True:
        fullArrayReading=_Sensor_Functions.getFullArrayReading()
        if fullArrayReading[0]==FailedDiagnosticSession:
            _Sonar_Dashboard_Functions.sonarFailure(fullArrayReading)
            break
        fullArrayReading=_Sonar_Dashboard_Functions.convertArrayToStringList(fullArrayReading)
        _Sonar_Dashboard_Functions.renderSonarDash()
        renderButtons()
        _Sonar_Dashboard_Functions.displayFullArrayValues(fullArrayReading)
    return
    
    


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y =event.pos
            if fa_clk.collidepoint(x,y):
                pollFullArray
            if fb_clk.collidepoint(x,y):
                screen.blit(ForwardButtonOn,(349,183))
                pygame.display.update()
                pygame.mixer.music.play()
                forwardArrayReading=_Sensor_Functions.monitorForwardArray()
                if forwardArrayReading[0]==FailedDiagnosticSession:
                    _Sonar_Dashboard_Functions.sonarFailure(forwardArrayReading[1])
                    break
                forwardArrayReading=_Sonar_Dashboard_Functions.convertArrayToStringList(forwardArrayReading)
                _Sonar_Dashboard_Functions.renderSonarDash()
                renderButtons()
                _Sonar_Dashboard_Functions.displayForwardArrayValues(forwardArrayReading)
            if rb_clk.collidepoint(x,y):
                screen.blit(RearButtonOn,(350,215))
                pygame.display.update()
                pygame.mixer.music.play()
                rearArrayReading=_Sensor_Functions.monitorRearArray()
                if rearArrayReading[0]==FailedDiagnosticSession:
                    _Sonar_Dashboard_Functions.sonarFailure(rearArrayReading[1])
                    break
                rearArrayReading=_Sonar_Dashboard_Functions.convertArrayToStringList(rearArrayReading)
                _Sonar_Dashboard_Functions.renderSonarDash()
                renderButtons()
                _Sonar_Dashboard_Functions.displayRearArrayValues(rearArrayReading)
    pygame.display.update()




    


        
    
    
