from asyncio import constants
from tkinter import BROWSE
import pygame, sys,os
from pygame.locals import * 
import random
import time

WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 102, 255)
DARK_BLUE = (0, 0, 153)
ORANGE = (255, 102, 0)
YELLOW = (255, 255, 0)
BROWN = (153, 51, 51)

def applyBackground(window):
    game_background = pygame.image.load("Images/game_background.png")
    window.blit(game_background,(0,0))

    profondeur = pygame.font.Font('pirate.ttf', 40)
    prof100m = profondeur.render("100m", True, WHITE)
    prof200m = profondeur.render("200m", True, WHITE)
    prof300m = profondeur.render("300m", True, WHITE)

    window.blit(prof100m, [250-prof100m.get_width()/2,250])
    window.blit(prof200m, [(pygame.display.get_surface().get_width()/2)-prof200m.get_width()/2,250])
    window.blit(prof300m, [1050-prof300m.get_width()/2,250])


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

def choosePlace(window,length,player,error):
    applyBackground(window)
    font = pygame.font.Font('menu.ttf', 50)
    title = font.render("Joueur "+str(player)+" place ton sous-marin de longueur: "+str(length), True, WHITE)
    window.blit(title, [(pygame.display.get_surface().get_width()/2)-title.get_width()/2,80])
    if(error):
        error = font.render("Erreur sur la selection, merci de recommencer", True, RED)
        window.blit(error, [(pygame.display.get_surface().get_width()/2)-title.get_width()/2,150])
    pygame.display.update()
    tuple = ()
    for i in range(length):
        result = retPos()
        pygame.draw.rect(window,RED,pygame.Rect(result[2]+2, result[3]+2, 28, 28))
        pygame.display.update()
        minor_tuple = (result[0], result[1])
        tuple =  tuple + (minor_tuple,)
    print(tuple)
    time.sleep(5)
    return tuple

# STATE = FALSE IF LOOSE TRUE IF WIN
def hit(state,window,matr,matr1,matr2,matr3,posX,posY,player):
    applyBackground(window)
    start = time.time()
    font = pygame.font.Font('menu.ttf', 50)
    if(state == False):
        result = font.render("Félicitation, beau tir ! ", True, WHITE)
        pygame.mixer.music.load('Song/explode.wav')
        pygame.mixer.music.play()
    else:
        result = font.render("Missile perdu ! ", True, RED)
        pygame.mixer.music.load('Song/plouf.wav')
        pygame.mixer.music.play()
    last_second = 0
    x = 0
    y = 300
    if(matr == 0):
        x = 100
    elif(matr == 1):
        x = 500
    else:
        x = 900
    while(int(time.time() - start) < 10):
        if(int((time.time()) - start) % 2 != last_second):
            printGame(window,matr1,matr2,matr3,player)
            window.blit(result, [(pygame.display.get_surface().get_width()/2)-result.get_width()/2,600])
            last_second = int((time.time()) - start) % 2
            if(last_second  == 0):
                if(state == False):
                    pygame.draw.rect(window,YELLOW,pygame.Rect(x + (posX * 30) + 2, y + (posY * 30) + 2, 28, 28))
                elif(state == True):
                    pygame.draw.rect(window,DARK_BLUE,pygame.Rect(x + (posX * 30) + 2, y + (posY * 30) + 2, 28, 28))
            pygame.display.update()
            



def printGame(window,matr1,matr2,matr3,player):
    applyBackground(window)
    x = -330
    x_temp = 0
    for tab in range(3):
        x = x + 400
        x_temp = x
        y = 270
        if(tab == 0):
            matr = matr1
        elif(tab == 1):
            matr = matr2
        else:
            matr = matr3
        for line in range (5):
            y = y + 30
            x_temp = x
            for column in range(10):
                x_temp = x_temp + 30
                if(matr[line][column] == 0):
                    pygame.draw.rect(window,BLUE,pygame.Rect(x_temp+2, y+2, 28, 28))
                elif(matr[line][column] == 1):
                    pygame.draw.rect(window,RED,pygame.Rect(x_temp+2, y+2, 28, 28))
                elif(matr[line][column] == 2):
                    pygame.draw.rect(window,ORANGE,pygame.Rect(x_temp+2, y+2, 28, 28))
                elif(matr[line][column] == 3):
                    pygame.draw.rect(window,BROWN,pygame.Rect(x_temp+2, y+2, 28, 28))
    pygame.display.update()

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
    for i in range(5):
        for j in range(10):
            if(x <= x_temp + 30 and x > x_temp and y <= y_temp + 30 and y > y_temp ):
                print(str(i) + str(j))
                return i,j,x_temp,y_temp
            x_temp = x_temp + 30
        x_temp = x_tab
        y_temp = y_temp +30


