import pygame
import sys
from testi2 import platform,Player
import random


class Kolikko:
    def __init__(self, coins,score):
        self.coins = coins[10]
        self.platform = platform
        self.surf = pygame.Surface
        self.player = Player
        self.score = score
        
        coin_img = pygame.image.load("pics/coin_img.jpg")
        if pygame.Surface[2] == 0 and random.randint(0,10) == 0:
            self.coins.append(coin_img[0],self.pos[0], self.pos[1]-15, coin_img.get_rect(x=self.pos[0], y=self.pos[1]-15))
    
    def drawCoins(self):
        for coin in self.coins:
            self.platform.blit((coin[0], coin[1], coin[2] - self.cameray))
            
    def updateCoins(self):
        for coin in self.coins[:]:
            if coin[3].colliderect(self.player):
                self.coins.remove(coin)
                self.score += 1
        self.coins = [coin for coin in self.coins if coin[3].bottom < 100]