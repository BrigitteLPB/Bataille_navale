import pygame
from pygame import mouse, draw, display, font, image, event
from pygame.locals import * 

from env import EnvUtilServer

WHITE = (255,255,255)
RED = (255, 0, 0)

def applyBackground(window: pygame.Surface):
    game_background = image.load(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Images/game_background.png")
    _ = window.blit(game_background,(0,0))

    profondeur = font.Font(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Font/pirate.ttf", 40)
    prof100m = profondeur.render("100m", True, WHITE)
    prof200m = profondeur.render("200m", True, WHITE)
    prof300m = profondeur.render("300m", True, WHITE)

    _ = window.blit(prof100m, [250-prof100m.get_width()/2,250])
    _ = window.blit(prof200m, [(display.get_surface().get_width()/2)-prof200m.get_width()/2,250])
    _ = window.blit(prof300m, [1050-prof300m.get_width()/2,250])


    x_pos = 100
    for _ in range(3):
        x=x_pos
        y=300
        for _ in range(6):
            _ = draw.line(window,WHITE,(x, y), (x+300, y), 2)
            y = y + 30
        x=x_pos
        y=300
        for _ in range(11):
            _ = draw.line(window,WHITE,(x, y), (x, y+150), 2)
            x = x + 30
        x_pos = x_pos + 400


    display.update()

def choosePlace(window: pygame.Surface,length,player,error):
    applyBackground(window)
    
    menu_font = font.Font(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Font/menu.ttf", 50)
    title = menu_font.render("Joueur "+str(player)+" place ton sous-marin de longueur: "+str(length), True, WHITE)
    _ = window.blit(title, [(display.get_surface().get_width()/2)-title.get_width()/2,80])
    
    if(error):
        error = menu_font.render("Erreur sur la selection, merci de recommencer", True, RED)
        _ = window.blit(error, [(display.get_surface().get_width()/2)-title.get_width()/2,150])
    display.update()
    positions = []
    
    for _ in range(length):
        result = retPos()
        _ = draw.rect(window,RED,pygame.Rect(result[2]+2, result[3]+2, 28, 28))
        display.update()
        positions.append((result[0], result[1]))
    
    # time.sleep(5)
    return positions



def retPos():
    wait = True
    while(wait == True):
        for e in event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = mouse.get_pos()
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
            if(x <= x_temp + 30 and x > x_temp and y <= y_temp + 30 and y > y_temp ):
                print(str(i) + str(j))
                return i,j,x_temp,y_temp
            x_temp = x_temp + 30
        x_temp = x_tab
        y_temp = y_temp +30


