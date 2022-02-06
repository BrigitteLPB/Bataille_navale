# from menu import *
from sdl_init import initVideo
# from end import *
from sdl_game import choosePlace

window = initVideo()
print(choosePlace(window,3,1,True))
#menu(window)
#end(window)