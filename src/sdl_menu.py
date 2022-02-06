# import pygame
# from pygame import KEYDOWN, K_UP, K_DOWN, K_RETURN, QUIT


import pygame

from env import EnvUtilServer


def menu(window):
    continuer = 1
    refresh = True
    pos_trait = 400
    pygame.mixer.music.load(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Song/menu.wav")
    pygame.mixer.music.play()
    while continuer:
        if(refresh):
            image_fond = pygame.image.load(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Images/fond_menu.png")
            fond = image_fond.convert()
            window.blit(fond,(0,0))
            pygame.display.flip()
            font = pygame.font.Font(f"{EnvUtilServer.env['ASSETS_FOLDER']}/Font/menu.ttf", 60)
            classical = font.render('Classical', True, (255, 255, 255))
            online = font.render('Online', True, (255, 255, 255))
            IA = font.render('IA Mode', True, (255, 255, 255))
            window.blit(classical, [50,325])
            window.blit(IA, [50,475])
            window.blit(online, [50,400])
            pygame.draw.line(window,(255, 0, 0),(50, pos_trait), (300, pos_trait), 4)
            pygame.display.update()
            refresh = False
        
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and pos_trait>400:
                    pos_trait = pos_trait - 75
                    refresh = True
                if event.key == pygame.K_DOWN and pos_trait<=475:
                    pos_trait = pos_trait + 75
                    refresh = True
                if event.key == pygame.K_RETURN:
                    print("test")
