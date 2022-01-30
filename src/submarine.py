

from enum import Enum
from sea_case import CannotHitCase, SeaCase, SeaCaseState

# from submarine_case import SubmarineCase

# from layer import Layer, WrongPosOnLayer


class SubmarineOrientation(str, Enum):
    NORTH	=	'north'
    EAST	=	'east'
    SOUTH	=	'south'
    WEST	=	'west'

class Submarine():

    def __init__(self, size: int):
        self.size: int = size
        self.submarine_case = [SeaCase(0, 0) for _ in range(size)]
        self.orientation = SubmarineOrientation.NORTH


    # def setPos(self, layer: Layer, pos_x: int, pos_y: int, orientation: SubmarineOrientation):
    #     """set compute the position of all cases on layer

    #     Args:
    #         layer (Layer): the layer to add a submarine
    #         x (int): x pos for last SubmarineCase
    #         y (int): y pos for last SubmarineCase
    #         orientation (SubmarineOrientation): orientation of the submarine
    #     """
    #     x = pos_x
    #     y = pos_y

    #     for case in reversed(self.submarine_case):
    #         # layer.add_submarine(case, x, y)

    #         if orientation == SubmarineOrientation.NORTH:
    #             x+=1
    #         if orientation == SubmarineOrientation.SOUTH:
    #             x-=1
    #         if orientation == SubmarineOrientation.WEST:
    #             y+=1
    #         if orientation == SubmarineOrientation.EAST:
    #             y-=1
        

    def __str__(self):
        return f"[Submarine]\u007Bsize:{self.size},orientation:{self.orientation},submarine_case:[{''.join(str(c) for c in self.submarine_case)}]\u007D"


class SubmarineCase(SeaCase):

    def __init__(self, submarine: Submarine, x: int, y: int):
        super().__init__(x, y)
        self.submarine = submarine


    def hit(self):
        if(self.state == SeaCaseState.HIDDEN):
            self.state = SeaCaseState.TOUCHED
        else:
            raise CannotHitCase(self)
        
    
    def __str__(self):
        return f"[SubmarineCase]\u007Bsubmarine:{str(self.submarine)},{super().__str__()}\u007D"


    
if __name__ == "__main__":
    print(Submarine(3))
    print(SubmarineCase(None, 1, 1)) # expected : Submarine:None,x:1,y:1,layer:None
