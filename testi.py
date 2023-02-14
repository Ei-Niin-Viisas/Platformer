
"""
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
"""
import threading, time

class testi:

    def __init__(self):
        self.numero = 0

    def coder(self):
        print("Coders: " + str(self.numero))
        self.numero += 1
        time.sleep(2)



threads = []
#for k in range(5):

testi = testi()

t = threading.Thread(target=testi.coder, args=())
threads.append(t)
t.start()

time.sleep(1)
print("hahaa")

k = threading.Thread(target=testi.coder, args=())
threads.append(k)
k.start()

t.join()
k.join()

print(testi.numero)