import math
import pygame
from pygame import font, display, event
from pygame.locals import * 

from env import EnvUtilServer
from sdl_init import initVideo


def end(window: pygame.Surface):
    refresh = True
    # color_num = 0
    # color_inc = True

    colors_inc = 0
    colors_inc_step = 150


    while(refresh):
        winner = 1
        ft = font.Font(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Font/menu.ttf", 60)
        # if(color_inc == True):
        #     color_num = color_num + 1
        #     if(color_num == 255):
        #         color_inc = False
        # else:
        #     color_num = color_num - 1
        #     if(color_num == 0):
        #         color_inc = True
        
        # end = ft.render('Fin du jeu', True, (235, color_num, 0))
        # winner = ft.render('Le joueur '+str(winner)+' est victorieux', True, (235, color_num, 0))

        colors =    (128 + int(127 * math.cos((colors_inc * math.pi)/(3*colors_inc_step))), 
                    128 + int(127 * math.cos(((2*math.pi)/3) + (colors_inc * math.pi)/(3*colors_inc_step))), 
                    128 + int(127 * math.cos(((4*math.pi)/3) + (colors_inc * math.pi)/(3*colors_inc_step))))

        colors_inc += 1

        end = ft.render('Fin du jeu', True, colors)
        winner = ft.render('Le joueur '+str(winner)+' est victorieux', True, colors)
    
        _ = window.blit(end, [(display.get_surface().get_width()/2)-end.get_width()/2,325])
        _ = window.blit(winner, [(display.get_surface().get_width()/2)-winner.get_width()/2,400])
        
        display.update()
        for e in event.get():               # On parcours la liste de tous les événements reçus
                if e.type == pygame.QUIT:   # Si un de ces événements est de type QUIT
                    refresh = 0             # On arrête la boucle

if __name__ == "__main__":
    w = initVideo()
    end(w)
