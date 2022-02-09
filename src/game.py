from enum import Enum
from pathlib import Path

import pygame
from constants import SEA
from env import EnvUtilServer
from log import LogUtil
from sea import Sea, SeaCaseId
from sdl import SDL, MenuOption

class JoueurId(int, Enum):
    JOUEUR_1 = 0
    JOUEUR_2 = 1

class Game():
    def __init__(self) -> None:
        self.joueurs = [Sea(SEA["LAYERS"]["HEIGHT"], SEA["LAYERS"]["WIDTH"], SEA["LAYERS"]["DEPTH"], SEA["SUBMARINES"]["SIZES"]) for _ in range(2)]
        self.endapp = False

        # setting up SDL
        try:
            assets_path = EnvUtilServer.env['ASSETS_FOLDER']
        except KeyError:
            assets_path = Path(__file__).parent / 'assets'

        self.sdl = SDL("Batialle Navale", Path(assets_path))

        for s in self.joueurs:
            s.on("update", self.updateEvent)
            s.on("hit", self.hitEvent)
            s.on("end", self.winEvent)
            s.on("miss", self.missEvent)
            s.on("sink", lambda _ : LogUtil.INFO("sink event"))

        self.actualTurn = JoueurId.JOUEUR_1

    def cleanPos(self, pos: list): 
        """extrait le layer d'un tryptique

        Args:
            pos (list): liste de tuple (layer, x, y)

        Returns:
            tuple[int, list[tuple[int, int]]]: (layer, [(x, y)])
        """                              
        layer = -1
        posXY = []
        
        for l, x, y in pos:
            if layer == -1:
                layer = l
            elif l != layer:
                return (None, None)
            
            posXY.append((x, y))
        
        return (layer, posXY)


    def run(self):
        choix = self.sdl.menuScreen()

        if choix == MenuOption.CLASSIC:
            self.classicMode()
        elif choix == MenuOption.IA_MODE:
            pass
        elif choix == MenuOption.QUIT:
            pygame.quit()

    def classicMode(self):
        # placement
        for j in range(len(self.joueurs)):
            self.sdl.updateEvent(self.joueurs[j])
            
            sea = self.joueurs[j]
            for sub_id in sea.submarines:
                error = True
                first = True

                while(error):
                    if error and not first:
                        self.sdl.updateEvent(self.joueurs[j])
                    self.sdl.printTextPlacement(j, sea.submarines[sub_id][0], error and not first)

                    pos = []
                    for _ in range(sea.submarines[sub_id][0]):
                        pos.append(self.sdl.pickCase())

                    layer, cleanPos = self.cleanPos(pos)
                    
                    if layer != None:
                        if sea.placeSubmarine(sub_id, sea.layers[layer], cleanPos):
                            error = False
                    
                    first = False

        LogUtil.INFO("submarines for both players placed")


        # jeu
        error = False
        while not self.endapp:
            s = self.joueurs[(self.actualTurn+1)%len(self.joueurs)]
            self.sdl.updateEvent(s)
            self.sdl.printTextTir(self.actualTurn, error)
            layer, x, y = self.sdl.pickCase()
            error = False
            
            if s.hit(s.layers[layer], x, y):
                self.actualTurn = (self.actualTurn + 1) % len(self.joueurs)
            else : 
                error = True
    
    # Events
    def hitEvent(self, args):
        (sea, layer, x, y) = args
        self.sdl.hit(sea, sea.layers.index(layer), x, y)

    def missEvent(self, args):
        (sea, layer, x, y) = args
        self.sdl.miss(sea, sea.layers.index(layer), x, y)

    def updateEvent(self, sea: Sea):
        self.sdl.updateEvent(sea)

    def winEvent(self, sea: Sea):
        for j in range(len(self.joueurs)):
            if self.joueurs[j] == sea:
                self.sdl.endScreen(j)
                self.endapp = True
                return  # endpoint here


if __name__ == "__main__":
    TEST_WIN = False
    TEST_PLACEMENT = True
    
    if TEST_WIN:
        g = Game()
        if g.joueurs[0].placeSubmarine(SeaCaseId.SUBMARINE_1, g.joueurs[0].layers[0], [(0, 0)]):
            if g.joueurs[0].hit(g.joueurs[0].layers[0], 0, 0):
                LogUtil.DEBUG("TEST WIN 1 : OK")
            else:
                LogUtil.ERROR("TEST WIN 1 : KO (hit)")
        else:
            LogUtil.ERROR("TEST WIN 1 : KO (placement)")

    if TEST_PLACEMENT:
        g = Game()
        g.run()