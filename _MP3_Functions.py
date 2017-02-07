import pygame

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
from time import sleep



while True:
    pygame.mixer.music.load("hailbeep.mp3")
    pygame.mixer.music.play()
    sleep(5)
    
