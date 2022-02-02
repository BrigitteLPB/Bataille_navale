

from enum import Enum

from event import Event


class SeaCaseState(str, Enum):
    HIDDEN	=	'hidden'
    SEEN	=	'seen'
    MISSED  =   'miss'
    TOUCHED =   'touched'


class CannotHitCase(Exception):
    def __init__(self, case):
        super().__init__(f'this case cannot be hit : {case}')


class SeaCase(Event):
    


    def __init__(self, pos_x: int, pos_y: int):
        """constructor of SeaCase

        Args:
            pos_x (int): x position of the case
            pos_y (int): y position of the case
        """        
        super().__init__()
        self.x : int = pos_x
        self.y: int = pos_y
        self.state : SeaCaseState = SeaCaseState.HIDDEN

    def hit(self):
        if(self.state == SeaCaseState.HIDDEN):
            self.state = SeaCaseState.MISSED
        else:
            raise CannotHitCase(self)
    
    # def set_pos(self, x, y):
    #     self.x = x
    #     self.y = y
    
    def __str__(self):
        return f"[SeaCase]\u007Bx:{self.x},y:{self.y}\u007D"


if __name__ == "__main__":
    # testing the print
    print(SeaCase(1, 1)) # expected : x:1,y:1
