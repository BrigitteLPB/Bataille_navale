import pygame, sys,os
from pygame.locals import * 
import random
import time
def end(window):
   refresh = True
   second = 0
   color_num = 0
   color_inc = True
   while(refresh):
        winner = 1
        font = pygame.font.Font('menu.ttf', 60)
        if(color_inc == True):
            color_num = color_num + 1
            if(color_num == 255):
                color_inc = False
        else:
            color_num = color_num - 1
            if(color_num == 0):
                color_inc = True
        end = font.render('Fin du jeu', True, (235, color_num, 0))
        winner = font.render('Le joueur '+str(winner)+' est victorieux', True, (235, color_num, 0))
        window.blit(end, [(pygame.display.get_surface().get_width()/2)-end.get_width()/2,325])
        window.blit(winner, [(pygame.display.get_surface().get_width()/2)-winner.get_width()/2,400])
        pygame.display.update()
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    refresh = 0      #On arrête la boucle

