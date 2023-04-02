import pygame, sys
import pygame


class Kolikko(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pics/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collision(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.kill()
            player.score += 10
