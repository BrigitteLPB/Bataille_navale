from asyncio import constants
import pygame, sys,os
from pygame.locals import * 
import random
import time

WHITE = (255,255,255)
RED = (255, 0, 0)

def applyBackground(window):
    game_background = pygame.image.load("Images/game_background.png")
    window.blit(game_background,(0,0))
    x_pos = 100
    for i in range(3):
        x=x_pos
        y=300
        for i in range(6):
            pygame.draw.line(window,WHITE,(x, y), (x+300, y), 2)
            y = y + 30
        x=x_pos
        y=300
        for j in range(11):
            pygame.draw.line(window,WHITE,(x, y), (x, y+150), 2)
            x = x + 30
        x_pos = x_pos + 400


    pygame.display.update()

def choosePlace(window,length):
    applyBackground(window)
    tuple = ()
    for i in range(length):
        result = retPos()
        pygame.draw.rect(window,RED,pygame.Rect(result[2]+2, result[3]+2, 28, 28))
        pygame.display.update()
        minor_tuple = (result[0], result[1])
        tuple =  tuple + (minor_tuple,)
    print(tuple)
    time.sleep(5)



def retPos():
    wait = True
    while(wait == True): 
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                print(x)
                wait = False
    tab_no = 0
    if(x < 450):
        tab_no = 1
        x_tab = 100
    elif(x < 850):
        tab_no = 2
        x_tab = 500
    else:
        tab_no = 3
        x_tab = 900
    print(tab_no)
    y_tab = 300

    x_temp = x_tab
    y_temp = y_tab
    for i in range(6):
        for j in range(10):
            if(x < x_temp + 30 and x > x_temp and y < y_temp + 30 and y > y_temp ):
                print(str(i) + str(j))
                return i,j,x_temp,y_temp
            x_temp = x_temp + 30
        x_temp = x_tab
        y_temp = y_temp +30


