import pygame, sys,os
from pygame.locals import * 
from menu import *
from init import *
from end import *
from game import *

window = initVideo()
#choosePlace(window,3,1,True)
matr = [[0 for i in range(10)] for j in range(5)]
matr[3][9] = 1
matr[2][3] = 2
print(matr)
printGame(window,matr,matr,matr,3)
#menu(window)
#end(window)