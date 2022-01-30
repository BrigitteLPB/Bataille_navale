

from enum import Enum
from pyclbr import Function

# from layer import Layer


class SeaCaseState(str, Enum):
    HIDDEN	=	'hidden'
    SEEN	=	'seen'
    MISSED  =   'miss'
    TOUCHED =   'touched'


class CannotHitCase(Exception):
    def __init__(self, case):
        super().__init__(f'this case cannot be hit : {case}')

class SeaCase():

    # def __init__(self, layer: Layer, pos_x: int, pos_y: int):
    def __init__(self, pos_x: int, pos_y: int):
        # self.layer : Layer = layer
        self.x : int = pos_x
        self.y: int = pos_y
        self.state : SeaCaseState = SeaCaseState.HIDDEN

    def hit(self):
        if(self.state == SeaCaseState.HIDDEN):
            self.state = SeaCaseState.MISSED
        else:
            raise CannotHitCase(self)
    
    def __str__(self):
        # return f"x:{self.x},y:{self.y},layer:{self.layer}"
        return f"[SeaCase]\u007Bx:{self.x},y:{self.y}\u007D"


if __name__ == "__main__":
    # testing the print
    # print(SeaCase(None, 1, 1)) # expected : x:1,y:1,layer:None
    print(SeaCase(1, 1)) # expected : x:1,y:1
