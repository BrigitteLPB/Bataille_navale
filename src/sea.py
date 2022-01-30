# this file describe a Class with all the layers
from enum import Enum
from constants import SEA
from sea_case import SeaCase
from submarine import Submarine


class SeaEndOfGame(Enum, str):
    NONE = 'none'
    WIN = 'win'
    LOSE = 'lose'


class SeaDisplayInterface():
    
    def __init__(self):
        pass

    def display_sea(self, sea: Sea):
        pass

    def display_error(self, err):
        pass

    def display_shot(self, sea: Sea, x: int, y:int):
        pass

    def display_endOfGame(self, sea: Sea, endOfGame: SeaEndOfGame):
        pass

class Sea():

    # def __init__(self):
    #     self.layers = [Layer(SEA['LAYERS']['WIDTH'], SEA['LAYERS']['HEIGHT'], x) for x in SEA['LAYERS']['DEPTH']]
    #     self.submarines = [Submarine(x) for x in SEA['SHIPS']['SIZES']]


    # def __str__(self):
    #     return f"[Sea]\u007Blayers:[{''.join(str(l) for l in self.layers)}],submarines:{''.join(str(s) for s in self.submarines)}\u007D"

    def __init__(self, width, heigth, layer_depth: list, submarine_size: list, display : SeaDisplayInterface):
        self.width = width
        self.heigth = heigth
        self.layer_depth = layer_depth
        self.sea_cases = [[[SeaCase(x, y) for x in range(self.width)] for y in range(self.heigth)] for _ in range(len(layer_depth))]
        self.submarines = [Submarine(size) for size in submarine_size]
        self.display = display

    def get_sea(self):
        return self.sea_cases

    def __str__(self):
        return f"[Sea]\u007Bcases:{self.sea_cases},submarines:{''.join(str(s) for s in self.submarines)}\u007D"



if __name__ == "__main__":
    s = Sea(SEA['LAYERS']['WIDTH'], SEA['LAYERS']['HEIGHT'], SEA['LAYERS']['DEPTH'], SEA['SUBMARINES']['SIZES'], SeaDisplayInterface())
    print(s)
