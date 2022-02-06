from enum import Enum
from constants import SDL, SEA
from sdl_end import end
from sea import Sea
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
                pass

        self.actualTurn = JoueurId.JOUEUR_1

    def makeTurn(self):
        pass

    def run(self):
        if SDL:
            end(self.windows)

if __name__ == "__main__":
    g = Game()
    g.run()