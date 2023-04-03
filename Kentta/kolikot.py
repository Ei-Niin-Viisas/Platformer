import pygame, sys
import pygame
#from Kentta.kentta import platform
import random


class Kolikko(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        

        self.image = pygame.image.load("pics/coin.png")
        self.surf = pygame.Surface((self.image.get_size()))
        self.surf = self.image
        self.rect = self.surf.get_rect()
        
        self.rect.center = (200,500)
        

    def collision(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.kill()
            #player.score += 10
            


