from enum import Enum
from constants import SDL, SEA
from log import LogUtil
from sdl_end import end
from sdl_game import choosePlace
from sdl_menu import MenuOption, menu
from sea import Sea, SeaCaseId
from sdl_init import initVideo

class JoueurId(int, Enum):
    JOUEUR_1 = 0
    JOUEUR_2 = 1

class Game():
    def __init__(self) -> None:
        self.joueurs = [Sea(SEA["LAYERS"]["HEIGHT"], SEA["LAYERS"]["WIDTH"], SEA["LAYERS"]["DEPTH"], SEA["SUBMARINES"]["SIZES"]) for _ in range(2)]
        self.endapp = False

        # setting up SDL
        if SDL:
            self.windows = initVideo()

            for s in self.joueurs:
                # s.on("update")
                s.on("end", self.checkWin)
                pass

        self.actualTurn = JoueurId.JOUEUR_1

    def makeTurn(self):
        pass

    def checkWin(self, sea: Sea):
        for j in range(len(self.joueurs)):
            if self.joueurs[j] == sea:
                end(self.windows, j+1)
                self.endapp = True
                return  # endpoint here

    def cleanPos(self, pos: list):                       
        layer = -1
        posXY = []
        
        for l, x, y in pos:
            if layer == -1:
                layer = l-1
            elif l-1 != layer:
                return (None, None)
            
            posXY.append((x, y))
        
        return (layer, posXY)


    def run(self):
        if SDL:
            choix = menu(self.windows)

            if choix == MenuOption.CLASSIC:
                self.classicMode()
            elif choix == MenuOption.IA_MODE:
                pass
            elif choix == MenuOption.ONLINE:
                pass

    def classicMode(self):
        # placement
        for j in range(len(self.joueurs)):
            sea = self.joueurs[j]
            for sub_id in sea.submarines:
                error = True
                first = True

                while(error):
                    pos = choosePlace(self.windows, sea.submarines[sub_id][0], j+1, error and not first)

                    layer, cleanPos = self.cleanPos(pos)
                    
                    if layer != None:
                        if sea.placeSubmarine(sub_id, sea.layers[layer], cleanPos):
                            error = False
                    
                    first = False
        LogUtil.INFO("submarines for both players placed")


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