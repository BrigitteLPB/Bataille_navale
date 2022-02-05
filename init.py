import pygame, sys,os
from pygame.locals import * 


def initVideo():
    pygame.init() 
    pygame.font.init() 
    window = pygame.display.set_mode([1280,720])
    pygame.display.set_caption('Bataille Navale')
    return window