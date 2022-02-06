# import pygame
# from pygame import KEYDOWN, K_UP, K_DOWN, K_RETURN, QUIT


from enum import Enum
import pygame
from pygame import mixer, image, draw, display, event, font

from env import EnvUtilServer
from sdl_init import initVideo

class MenuOption(int, Enum):
    CLASSIC = 0
    ONLINE = 1
    IA_MODE = 2

def menu(window: pygame.Surface):
    continuer = 1
    refresh = True
    pos_trait = 400
    mixer.music.load(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Song/menu.wav")
    mixer.music.play()
    while continuer:
        if(refresh):
            image_fond = image.load(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Images/fond_menu.png")
            fond = image_fond.convert()
            _ = window.blit(fond,(0,0))
            display.flip()
            ft = font.Font(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Font/menu.ttf", 60)
            classical = ft.render('Classical', True, (255, 255, 255))
            online = ft.render('Online', True, (255, 255, 255))
            IA = ft.render('IA Mode', True, (255, 255, 255))
            _ = window.blit(classical, [50,325])
            _ = window.blit(IA, [50,475])
            _ = window.blit(online, [50,400])
            _ = draw.line(window,(255, 0, 0),(50, pos_trait), (300, pos_trait), 4)
            display.update()
            refresh = False
        
        for e in event.get():   #On parcours la liste de tous les événements reçus
            if e.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and pos_trait>400:
                    pos_trait = pos_trait - 75
                    refresh = True
                if e.key == pygame.K_DOWN and pos_trait<=475:
                    pos_trait = pos_trait + 75
                    refresh = True
                if e.key == pygame.K_RETURN:
                    return MenuOption.CLASSIC    # TODO renvoyer le choix

if __name__ == "__main__":
    w = initVideo()
    _ = menu(w)