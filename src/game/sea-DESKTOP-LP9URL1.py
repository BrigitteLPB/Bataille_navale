# this file describe a Class with all the layers
from enum import Enum
from sea_case import SeaCaseState
from submarine import SubmarineOrientation
from submarine_case import SubmarineCase
from sea_case import SeaCase
from submarine import Submarine
from event import Event

# TODO event programming

class SeaEndOfGame(str, Enum):
    NONE = 'none'
    WIN = 'win'
    LOSE = 'lose'


class Sea(Event):
    """Sea class
    Events: 
        - update : emitted the sea is updated
    """

    def __init__(self, width: int, heigth: int, layer_depth: list, submarine_size: list):
        """Sea constructor

        Args:
            width (int): largeur du plateau
            heigth (int): longeur du plateau
            layer_depth (list): pronfondeur des chacunes des couches
            submarine_size (list): taille de chacun des sous-marins
        """
        super().__init__()
           
        self.width = width
        self.heigth = heigth
        self.layer_depth = layer_depth
        self.sea_cases = [[[SeaCase(x, y) for x in range(self.width)] for y in range(self.heigth)] for _ in range(len(layer_depth))]
        self.submarines = [Submarine(self, size) for size in submarine_size]
   
    def place_submarine(self, submarine: Submarine, orientation: SubmarineOrientation, layer: int, x: int, y: int) -> bool:
        opperation_success = False

        # checking out of bounds
        if x >= 0 and x < self.width and y >= 0 and y < self.heigth:
            # checking out of bounds before assinement
            if(orientation == SubmarineOrientation.NORTH and y - submarine.size >= 0) or (orientation == SubmarineOrientation.SOUTH and y + submarine.size < self.heigth) or (orientation == SubmarineOrientation.EAST and x - submarine.size >= 0) or (orientation == SubmarineOrientation.WEST and x + submarine.size < self.width):
                cases_layer = s.sea_cases[s.layer_depth.index(layer)]
                
                submarine.update_pos(x, y, orientation)
                
                # place the submarine on the sea
                cases = filter(lambda sea_case, pos : (sea_case.x, sea_case.y) in pos, cases_layer, [(s.x, s.y) for s in submarine.submarine_case])
               
                isFree = True
                for c in cases :
                    if isinstance(c, SubmarineCase):
                        isFree = False

                if isFree:
                    for new_c in submarine.submarine_case:
                        self.sea_cases[new_c.y][new_c.x] = new_c
                    opperation_success = True
        
        try:
            self.emit('update', self)
        except KeyError:
            pass

        return opperation_success




    
    def __str__(self):
        # return f"[Sea]\u007Bcases:{self.sea_cases},submarines:{''.join(str(s) for s in self.submarines)}\u007D"
        return f"[Sea]\u007Bcases:{self.sea_cases},submarines:{self.submarines}\u007D"


if __name__ == "__main__":
    # print function
    def show_sea(sea: Sea):
        for layer in sea.sea_cases:
            for line in layer:
                for case in line:
                    if case.state == SeaCaseState.TOUCHED:
                        print("X", end="")
                    elif case.state == SeaCaseState.SEEN :
                        print("O", end="")
                    elif case.state == SeaCaseState.MISSED:
                        print(".", end='')
                    elif case.state == SeaCaseState.HIDDEN:
                        if isinstance(case, SubmarineCase):
                            print('#', end='')
                        else:
                            print('~', end="")
                print()
            print('-' * sea.width)



    # s = Sea(SEA['LAYERS']['WIDTH'], SEA['LAYERS']['HEIGHT'], SEA['LAYERS']['DEPTH'], SEA['SUBMARINES']['SIZES'])
    s = Sea(10, 10, [100, 200, 300], [1, 2, 2, 3, 3])
    print(s)


    # test de placment de sous-marins
    s.on('update', show_sea)

    if s.place_submarine(s.submarines[0], SubmarineOrientation.NORTH, s.layer_depth[0], 0, 0) :
        print("the submarine is correctly place")
    else:
        print("error during placing")
