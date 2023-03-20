import pygame, time
from pygame.locals import *

#Player tiedosto, sisältää tarvittavat tiedot ja variaabelit itse pelaajaa varten

 # 2 for two dimensional

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vec = pygame.math.Vector2
        self.animaatio = [  pygame.image.load("pics/run_frames/tile000.png"), pygame.image.load("pics/run_frames/tile001.png"), pygame.image.load("pics/run_frames/tile002.png"),
                            pygame.image.load("pics/run_frames/tile003.png"), pygame.image.load("pics/run_frames/tile004.png"), pygame.image.load("pics/run_frames/tile005.png"),
                            pygame.image.load("pics/run_frames/tile006.png"), pygame.image.load("pics/run_frames/tile007.png"), pygame.image.load("pics/run_frames/tile008.png"),
                            pygame.image.load("pics/run_frames/tile009.png"), pygame.image.load("pics/run_frames/tile010.png"), pygame.image.load("pics/run_frames/tile011.png")]
        
        self.paikallaan = [ pygame.image.load("pics/idle_frames/tile000.png"), pygame.image.load("pics/idle_frames/tile001.png"), pygame.image.load("pics/idle_frames/tile002.png"),
                            pygame.image.load("pics/idle_frames/tile003.png"), pygame.image.load("pics/idle_frames/tile004.png"), pygame.image.load("pics/idle_frames/tile005.png"),
                            pygame.image.load("pics/idle_frames/tile006.png"), pygame.image.load("pics/idle_frames/tile007.png"), pygame.image.load("pics/idle_frames/tile008.png"),
                            pygame.image.load("pics/idle_frames/tile009.png"), pygame.image.load("pics/idle_frames/tile010.png")]


        self.surf = pygame.Surface((35, 35))
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

        if pressed_keys[K_LSHIFT] or pressed_keys[K_RSHIFT]:
            self.ACC = 1
            self.counter += 1
        else:
            self.ACC = 0.5

        if (pressed_keys[K_LEFT] or pressed_keys[K_a]) and (pressed_keys[K_RIGHT] or pressed_keys[K_d]):
            self.seiso()
        elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -self.ACC
            self.suunta = False
            self.animoi()
        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = self.ACC
            self.suunta = True
            self.animoi()
        else:
             self.seiso()
        
        if pressed_keys[K_SPACE]:
            if hits:
                self.vel.y = -15

        #if (not pressed_keys[K_RIGHT] and not pressed_keys[K_d]) and (not pressed_keys[K_LEFT] and not pressed_keys[K_a]):
        #    self.seiso()
        #else:
        #    self.animoi()

        if self.pos.x > self.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.WIDTH
        
        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top+1
                self.vel.y = 0
            
        self.rect.midbottom = self.pos

    def animoi(self):
        if self.suunta == True:
            if self.counter%5 and (self.counter != 0 or self.counter > 60):
                self.surf = self.animaatio[int((self.counter/5)-1)]
        else:
            if self.counter%5 and (self.counter != 0 or self.counter < 60):
                self.surf = pygame.transform.flip(self.animaatio[int(self.counter/5-1)], True, False)
        
        if self.counter >= 60:
                    self.counter = 0
        self.counter += 1


    def seiso(self):
        if self.suunta == True:
            if self.counter%5 and (self.counter != 0 or self.counter > 60):
                self.surf = self.paikallaan[int((self.counter/5)-1)]
        else:
            if self.counter%5 and (self.counter != 0 or self.counter > 60):
                self.surf = pygame.transform.flip(self.paikallaan[int(self.counter/5-1)], True, False)
        
        if self.counter >= 55:
                    self.counter = 0
        self.counter += 1
