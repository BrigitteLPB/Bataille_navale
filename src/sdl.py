from enum import Enum
from pathlib import Path
from time import time
import pygame
from pygame import init, font, display, event, mixer, image, draw, mouse
import math
from sea import Sea, SeaCaseId

from log import LogUtil

class MenuOption(int, Enum):
    CLASSIC = 0
    ONLINE = 1
    IA_MODE = 2

WHITE = (255,255,255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 128)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)
BROWN = (128, 64, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)


class SDL():
    def __init__(self, caption: str, asset_path: Path) -> None:
        _ = init() 
        self.asset_path = asset_path
        font.init() 
        self.window = display.set_mode([1280, 720]) # hard coded dim due to shitty code, everything broke if dims change
        display.set_caption(caption)
    
    def endScreen(self, winner_id: int):
        """affiche le gagnant

        Args:
            window (pygame.Surface): pygame object
            winner (int): joueur : 0 = J1, 1 = J2
        """    
        refresh = True
        # color_num = 0
        # color_inc = True

        colors_inc = 0
        colors_inc_step = 150


        while(refresh):
            ft = font.Font((self.asset_path / "Font/menu.ttf").resolve(), 60)
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
            winner = ft.render('Le joueur '+str(winner_id + 1)+' est victorieux', True, colors)
        
            _ = self.window.blit(end, [(display.get_surface().get_width()/2)-end.get_width()/2,325])
            _ = self.window.blit(winner, [(display.get_surface().get_width()/2)-winner.get_width()/2,400])
            
            display.update()
            for e in event.get():               # On parcours la liste de tous les événements reçus
                    if e.type == pygame.QUIT:   # Si un de ces événements est de type QUIT
                        refresh = 0             # On arrête la boucle

    def menuScreen(self):
        """affiche le menu de début

        Returns:
            [MenuOption]: le choix du joueur
        """        
        continuer = 1
        refresh = True
        pos_trait = 400
        mixer.music.load(self.asset_path / "Song/menu.wav")
        mixer.music.play()
        while continuer:
            if(refresh):
                image_fond = image.load(self.asset_path / "Images/fond_menu.png")
                fond = image_fond.convert()
                _ = self.window.blit(fond,(0,0))
                display.flip()
                ft = font.Font(self.asset_path / "Font/menu.ttf", 60)
                classical = ft.render('Classical', True, (255, 255, 255))
                online = ft.render('Online', True, (255, 255, 255))
                IA = ft.render('IA Mode', True, (255, 255, 255))
                _ = self.window.blit(classical, [50,325])
                _ = self.window.blit(IA, [50,475])
                _ = self.window.blit(online, [50,400])
                _ = draw.line(self.window,(255, 0, 0),(50, pos_trait), (300, pos_trait), 4)
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

    def applyBackground(self):
        """affiche le fond d'écran du jeu

        Args:
            window (pygame.Surface): fenêtre pygame
        """    
        game_background = image.load(self.asset_path / "Images/game_background.png")
        _ = self.window.blit(game_background,(0,0))

        profondeur = font.Font(self.asset_path / "Font/pirate.ttf", 40)
        prof100m = profondeur.render("100m", True, WHITE)
        prof200m = profondeur.render("200m", True, WHITE)
        prof300m = profondeur.render("300m", True, WHITE)

        _ = self.window.blit(prof100m, [250-prof100m.get_width()/2,250])
        _ = self.window.blit(prof200m, [(display.get_surface().get_width()/2)-prof200m.get_width()/2,250])
        _ = self.window.blit(prof300m, [1050-prof300m.get_width()/2,250])


        x_pos = 100
        for _ in range(3):
            x=x_pos
            y=300
            for _ in range(6):
                _ = draw.line(self.window,WHITE,(x, y), (x+300, y), 2)
                y = y + 30
            x=x_pos
            y=300
            for _ in range(11):
                _ = draw.line(self.window,WHITE,(x, y), (x, y+150), 2)
                x = x + 30
            x_pos = x_pos + 400

    def printCase(self, layer, x, y, color, update = True):
        """affiche une case

        Args:
            layer (int): layer n° [0,2]
            x (int): x position [0,width]
            y (int): y position [0,height]
            color (tuple[int, int, int]): color to show
        """
        layer_offset_x = [100, 500, 900]
        layer_offset_y = [300, 300, 300]

        _ = draw.rect(self.window,color,pygame.Rect((layer_offset_x[layer] + 30 * x) +2, (layer_offset_y[layer] + 30 * y) +2, 28, 28))
        if update:
            display.update()

    def retPos(self):
        """retourne une case cliquée

        Returns:
            [tuple[Literal[1, 2, 3], int, int] | None]: retourne la position du clic : [n° layer, x, y], None si le clic est en dehors
        """        
        wait = True
        while(wait == True):
            for e in event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    x,y = mouse.get_pos()
                    print(x)
                    wait = False
                if e.type == pygame.QUIT:   # Si un de ces événements est de type QUIT
                    exit(0)

        tab_no = 0
        if(x < 450):
            tab_no = 0
            x_tab = 100
        elif(x < 850):
            tab_no = 1
            x_tab = 500
        else:
            tab_no = 2
            x_tab = 900
        # print(tab_no)
        y_tab = 300

        x_temp = x_tab
        y_temp = y_tab
        for i in range(6):
            for j in range(10):
                if(x <= x_temp + 30 and x > x_temp and y <= y_temp + 30 and y > y_temp ):
                    LogUtil.INFO(f"clic on : tab_no : {tab_no}, x: {i}, y: {j}") # DEBUG
                    return tab_no, j, i
                
                x_temp = x_temp + 30
            x_temp = x_tab
            y_temp = y_temp +30

    def pickCase(self):
        """sélectionne un case

        Returns:
            tuple[int,int,int]: trytique layer, x, y
        """        
        position = None
        while(position == None):
            position = self.retPos()
        
        (layer, x, y) = position
        self.showPlacement(layer, x, y)

        return position

    def showPlacement(self, layer, x, y):
        """affiche la case sélectionner par le placement

        Args:
            layer ([type]): n° du layer [0,2]
            x ([type]): x position [0,width]
            y ([type]): y postion [0,height]
        """        
        self.printCase(layer, x, y, RED)

    def printTextPlacement(self, id_joueur: int, submarine_lenght: int, error):
        """affiche le texte de placement du sousmarin

        Args:
            id_joueur (int): identifiant du joueur [0,n]
            submarine_lenght (int): longeur du sous marin [1,3]
            error (bool): print the error message
        """        
        menu_font = font.Font(self.asset_path / "Font/menu.ttf", 50)
        title = menu_font.render("Joueur "+str(id_joueur + 1)+" place ton sous-marin de longueur: "+str(submarine_lenght), True, WHITE)
        _ = self.window.blit(title, [(display.get_surface().get_width()/2)-title.get_width()/2,80])

        if error:
            error = menu_font.render("Erreur sur la selection, merci de recommencer", True, RED)
            _ = self.window.blit(error, [(display.get_surface().get_width()/2)-title.get_width()/2,150])

        display.update()

    def printTextTir(self, id_joueur: int, error: bool):
        """affiche le texte de tir

        Args:
            id_joueur (int): identifiant du joueur [0,1]
            error (bool): si on doit afficher le texte d'erreur
        """        
        menu_font = font.Font(self.asset_path / "Font/menu.ttf", 50)
        title = menu_font.render(f"C'est au tour du joueur {id_joueur+1} de tirer", True, WHITE)
        _ = self.window.blit(title, [(display.get_surface().get_width()/2)-title.get_width()/2,80])

        if error:
            error = menu_font.render("Erreur sur la selection, merci de recommencer", True, RED)
            _ = self.window.blit(error, [(display.get_surface().get_width()/2)-title.get_width()/2,150])

        display.update()

    # Events
    def updateEvent(self, sea:Sea):
        """evénement update de sea

        Args:
            sea (Sea): l'objet Sea
        """        
        self.applyBackground()
        
        for layer_id in range(len(sea.layers)):
            layer = sea.board[sea.layers[layer_id]]
            
            for y in range(len(layer)):
                for x in range(len(layer[y])):
                    case = layer[y][x]
                    if case[1] == True:
                        if case[0] == SeaCaseId.WATER:
                            self.printCase(layer_id, x, y, WHITE, False)
                        else:
                            self.printCase(layer_id, x, y, RED, False)
                    else:
                        if(case[0] == SeaCaseId.WATER):
                            self.printCase(layer_id, x, y, BLUE, False)
                        elif(case[0] == SeaCaseId.SUBMARINE_1):
                            self.printCase(layer_id, x, y, GREEN, False)
                        elif(case[0] == SeaCaseId.SUBMARINE_2):
                            self.printCase(layer_id, x, y, ORANGE, False)
                        elif(case[0] == SeaCaseId.SUBMARINE_3):
                            self.printCase(layer_id, x, y, BROWN, False)
        display.update()

    def hit(self, sea: Sea, layer, x, y):
        """génère le hit du joueur

        Args:
            state ([type]): FALSE IF LOOSE TRUE IF WIN
            window (pygame.Surface): fenêtre pygame
            matr ([type]): layer où toucher
            matr1 ([type]): layer 1
            matr2 ([type]): layer 2
            matr3 ([type]): layer 3
            posX ([type]): position X du tire
            posY ([type]): position Y du tire
            player ([type]): joueur 
        """    
        start = int(time())

        ft = font.Font(self.asset_path / "Font/menu.ttf", 50)
        result = ft.render("Félicitation, beau tir ! ", True, WHITE)
        _ = self.window.blit(result, [(display.get_surface().get_width()/2)-result.get_width()/2,600])

        mixer.music.load(self.asset_path / "Song/explode.wav")
        mixer.music.play()

    def miss(self, sea: Sea, layer, x, y):
        """génère le miss du joueur

        Args:
            state ([type]): FALSE IF LOOSE TRUE IF WIN
            window (pygame.Surface): fenêtre pygame
            matr ([type]): layer où toucher
            matr1 ([type]): layer 1
            matr2 ([type]): layer 2
            matr3 ([type]): layer 3
            posX ([type]): position X du tire
            posY ([type]): position Y du tire
            player ([type]): joueur 
        """    
        ft = font.Font(self.asset_path / "Font/menu.ttf", 50)
        result = ft.render("Missile perdu ! ", True, RED)
        _ = self.window.blit(result, [(display.get_surface().get_width()/2)-result.get_width()/2,600])
        
        mixer.music.load(self.asset_path / "Song/plouf.wav")
        mixer.music.play()

if __name__ == "__main__":
    from time import sleep
    from env import EnvUtilServer

    TEST_PRINT = True


    if TEST_PRINT:
        sdl = SDL("Test Print", Path(EnvUtilServer.env['ASSETS_FOLDER']))
        
        s = Sea(5, 10, [100, 200, 300], [1, 2, 3])
        
        _ = s.placeSubmarine(1, s.layers[0], [(0,0)])
        _ = s.placeSubmarine(2, s.layers[1], [(0,0), (1, 0)])
        _ = s.placeSubmarine(3, s.layers[2], [(0,0), (1, 0), (2, 0)])
        
        sdl.updateEvent(s)

        sdl.printTextPlacement(0, 3, False)
        print(sdl.pickCase())
        sleep(2)