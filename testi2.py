import pygame
from pygame.locals import *
import sys

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.vec = pygame.math.Vector2

        self.pos = self.vec((10, 200))
        self.vel = self.vec(0,0)
        self.acc = self.vec(0,0)

        self.ACC = 0.5
        self.FRIC = -0.12

    def move(self):
        self.acc = self.vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_LEFT]:
            self.acc.x = -self.ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = self.ACC

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1 , platforms, False)
        if P1.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top+1
                self.vel.y = 0

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

class tausta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()



PT1 = platform()
P1 = Player()
#P2 = Player()

platforms = pygame.sprite.Group()
platforms.add(PT1)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
#all_sprites.add(P2)

	

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
     
    jotain = displaysurface.fill((0,0,0))
 
    testi = []
    testi.append(jotain)
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        testi.append(entity.rect)
 
    pygame.display.update(testi)
    FramePerSec.tick(FPS)
    P1.move()
    P1.update()
