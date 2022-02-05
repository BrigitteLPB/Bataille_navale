from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:   
    from sea import Sea

from submarine_case import SubmarineCase
from enum import Enum

class SubmarineOrientation(str, Enum):
    NORTH	=	'north'
    EAST	=	'east'
    SOUTH	=	'south'
    WEST	=	'west'

class Submarine():

    def __init__(self, sea: Sea, size: int):
        self.sea = sea
        self.size: int = size
        self.submarine_case = [SubmarineCase(self, 0, 0) for _ in range(size)]
        self.orientation = SubmarineOrientation.NORTH

    def update_pos(self, pos_x: int, pos_y: int, orientation: SubmarineOrientation):
        """set compute the position of all cases on layer
        place the tail on the x/y pos. Orientation is determine by the direction tail to head

        Args:
            layer (Layer): the layer to add a submarine
            x (int): x pos for last SubmarineCase
            y (int): y pos for last SubmarineCase
            orientation (SubmarineOrientation): orientation of the submarine
        """
        x = pos_x
        y = pos_y

        for case in reversed(self.submarine_case):
            case.x = x
            case.y = y
            
            if orientation == SubmarineOrientation.NORTH:
                y-=1
            if orientation == SubmarineOrientation.SOUTH:
                y+=1
            if orientation == SubmarineOrientation.WEST:
                x+=1
            if orientation == SubmarineOrientation.EAST:
                x-=1
        

    def __str__(self):
        return f"[Submarine]\u007Bsea:{self.sea},size:{self.size},orientation:{self.orientation},submarine_case:[{self.submarine_case}]\u007D"


if __name__ == "__main__":
    print(Submarine(None, 3))
