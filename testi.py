print("Hello World")
print("Jelou wöörldi")
print("jotain")

import os, time
import pygame
x = 1000
y = 45
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
screen = pygame.display.set_mode((100,400))

time.sleep(2)