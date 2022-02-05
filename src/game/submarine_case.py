from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from submarine import Submarine

from sea_case import CannotHitCase, SeaCase, SeaCaseState

class SubmarineCase(SeaCase):

    def __init__(self, submarine: Submarine, x: int, y: int):
        super().__init__(x, y)
        self.submarine = submarine


    def hit(self):
        if(self.state == SeaCaseState.HIDDEN):
            self.state = SeaCaseState.TOUCHED
            if self.submarine:
                self.submarine.hit()
        else:
            raise CannotHitCase(self)
        
    
    def __str__(self):
        return f"[SubmarineCase]\u007Bsubmarine:{str(self.submarine)},{super().__str__()}\u007D"

if __name__ == "__main__":
    print(SubmarineCase(None, 1, 1)) # expected : Submarine:None,x:1,y:1,layer:None

