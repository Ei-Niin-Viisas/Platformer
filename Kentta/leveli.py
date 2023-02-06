import pygame, sys
from pygame.locals import *
from testi2 import Player, platform


#Luokka 
class taso:
    #Tähän tason luonti sitten, kun se on tehty
    def __init__(self, taso:list, player):
        pass

    #Tähän tulee sandbox, jossa voi testa muita oliota
    def __init__(self, platform):
        self.PT1 = platform

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.PT1)

    #Testi-metodi, joka piirtää punaisen "lattian"
    def testi(self, SCREEN):    
            for entity in self.all_sprites:
                SCREEN.blit(entity.surf, entity.rect)


    #Teen tähän valikon
    def valikko(self):
        pass


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((1280, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (1280/2, 720 - 10))
        self.counter = True

    #Metodi, joka vaihtaa platformin väriä
    def vaihdaVari(self):
        if self.counter:
            self.surf.fill((0,255,255))
            self.counter = False
        else:
            self.surf.fill((255,0,0))
            self.counter = True
