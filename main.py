import pygame, sys,os
from pygame.locals import * 
from menu import *
from init import *
from end import *
from game import *

window = initVideo()
time.sleep(3)
#choosePlace(window,3,1,True)
matr = [[0 for i in range(10)] for j in range(5)]
matr[3][9] = 1
matr[2][3] = 2
#print(matr)
hit(True,window,0,matr,matr,matr,1,2,4)
#printGame(window,matr,matr,matr,3)
#menu(window)
#end(window)