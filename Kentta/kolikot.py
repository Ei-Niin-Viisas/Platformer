import pygame, sys
import pygame
from Kentta.kentta import platform
import random


class Kolikko(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("pics/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = platform(width(200))
        self.rect.y = platform(height(150))
        

    """def collision(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.kill()
            player.score += 10"""


