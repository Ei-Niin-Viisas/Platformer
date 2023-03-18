import pygame
from pygame.locals import *

#Player tiedosto, sisältää tarvittavat tiedot ja variaabelit itse pelaajaa varten

 # 2 for two dimensional

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vec = pygame.math.Vector2
        self.animaatio = [pygame.image.load("pics/mario_1.jpg"),
            pygame.image.load("pics/mario_2.jpg"), pygame.image.load("pics/mario_3.jpg")]


        self.surf = pygame.Surface((80, 95))
        self.rect = self.surf.get_rect()
        self.surf.blit(self.animaatio[0], self.rect)
   
        self.pos = self.vec((10, 200))
        self.vel = self.vec(0,0)
        self.acc = self.vec(0,0)

        self.ACC = 0.5
        self.FRIC = -0.12

        self.WIDTH, self.HEIGHT  = pygame.display.get_window_size()

        self.counter = 0
        self.suunta = True

    def move(self, alustat):
        hits = pygame.sprite.spritecollide(self, alustat, False)

        self.acc = self.vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -self.ACC
            self.suunta = False
        if pressed_keys[K_RIGHT or K_d] or pressed_keys[K_d]:
            self.acc.x = self.ACC
            self.suunta = True
        if pressed_keys[K_SPACE]:
            if hits:
                self.vel.y = -15

        if (not pressed_keys[K_RIGHT] and not pressed_keys[K_d]) and (not pressed_keys[K_LEFT] and not pressed_keys[K_a]):
            if self.suunta:
                self.surf = self.animaatio[0]
            else:
                self.surf = pygame.transform.flip(self.animaatio[0], True, False)
        else:
            self.animoi(self.suunta)

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

    def animoi(self, suunta):
        if suunta == True:
            if self.counter == 0:
                self.surf = self.animaatio[1]
            elif self.counter == 6:
                self.surf = self.animaatio[2]
            elif self.counter == 12:
                self.surf = self.animaatio[1]
            elif self.counter == 18:
                self.surf = self.animaatio[0]
            elif self.counter == 24:
                self.counter = -1
        else:
            if self.counter == 0:
                self.surf = pygame.transform.flip(self.animaatio[1], True, False)
            elif self.counter == 6:
                self.surf = pygame.transform.flip(self.animaatio[2], True, False)
            elif self.counter == 12:
                self.surf = pygame.transform.flip(self.animaatio[1], True, False)
            elif self.counter == 18:
                self.surf = pygame.transform.flip(self.animaatio[0], True, False)
            elif self.counter == 24:
                self.counter = -1

        self.counter += 1
