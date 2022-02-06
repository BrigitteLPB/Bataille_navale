from enum import Enum
from constants import SDL, SEA
from log import LogUtil
from sdl_end import end
from sea import Sea, SeaCaseId
from sdl_init import initVideo

class JoueurId(int, Enum):
    JOUEUR_1 = 0
    JOUEUR_2 = 1

class Game():
    def __init__(self) -> None:
        self.joueurs = [Sea(SEA["LAYERS"]["HEIGHT"], SEA["LAYERS"]["WIDTH"], SEA["LAYERS"]["DEPTH"], SEA["SUBMARINES"]["SIZES"]) for _ in range(2)]

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
                return  # endpoint here

    def run(self):
        if SDL:
            pass

if __name__ == "__main__":
    TEST_WIN = True
    
    if TEST_WIN:
        g = Game()
        if g.joueurs[0].placeSubmarine(SeaCaseId.SUBMARINE_1, g.joueurs[0].layers[0], [(0, 0)]):
            if g.joueurs[0].hit(g.joueurs[0].layers[0], 0, 0):
                LogUtil.DEBUG("TEST WIN 1 : OK")
            else:
                LogUtil.ERROR("TEST WIN 1 : KO (hit)")
        else:
            LogUtil.ERROR("TEST WIN 1 : KO (placement)")
