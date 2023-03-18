import pygame
from pygame.locals import *

#Player tiedosto, sisältää tarvittavat tiedot ja variaabelit itse pelaajaa varten

 # 2 for two dimensional

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vec = pygame.math.Vector2
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = self.vec((10, 200))
        self.vel = self.vec(0,0)
        self.acc = self.vec(0,0)

        self.ACC = 0.5
        self.FRIC = -0.12

        self.WIDTH, self.HEIGHT  = pygame.display.get_window_size()

    def move(self, alustat):
        hits = pygame.sprite.spritecollide(self, alustat, False)

        self.acc = self.vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.acc.x = -self.ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = self.ACC
        if pressed_keys[K_SPACE]:
            if hits:
                self.vel.y = -15

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > self.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.WIDTH

        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top+1
                self.vel.y = 0
            
        self.rect.midbottom = self.pos

