from pygame import init, font, display
from pygame.locals import * 


def initVideo():
    _ = init() 
    font.init() 
    window = display.set_mode([1280,720])
    display.set_caption('Bataille Navale')
    return window