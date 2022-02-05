

from enum import Enum
from constants import SEA
from sea import Sea

class JoueurId(int, Enum):
    JOUEUR_1 = 0
    JOUEUR_2 = 1

class Game():
    def __init__(self) -> None:
        self.joueurs = [Sea(SEA["LAYERS"]["HEIGHT"], SEA["LAYERS"]["WIDTH"], SEA["LAYERS"]["DEPTH"], SEA["SUBMARINES"]["SIZES"]) for _ in range(2)]
        self.actualTurn = JoueurId.JOUEUR_1

    def makeTurn(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    pass