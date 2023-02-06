import pygame

#Player tiedosto, sisältää tarvittavat tiedot ja variaabelit itse pelaajaa varten

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 200))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
