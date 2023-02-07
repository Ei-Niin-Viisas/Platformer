import pygame, sys
from pygame.locals import *
from Valikot.peliValikko import pauseValikko

#Luokka 
class taso:
    #Tähän tason luonti sitten, kun se on tehty
    def __init__(self, taso:list, player):
        pass

    #Sandboxin konstruktori
    def __init__(self, screen, widht, height):
        self.SCREEN = screen
        self.WIDHT =  widht
        self.HEIGHT = height
        self.PT1 = platform(widht, height)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.PT1)
        self.FramePerSec = pygame.time.Clock()

    #Testi-metodi, joka piirtää punaisen "lattian"
    def testi(self):
        pygame.display.set_caption("Peli")

        while True:
            self.SCREEN.fill((0,0,0))
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_SPACE:
                        self.PT1.vaihdaVari()
                    elif event.key == pygame.K_ESCAPE:
                        pause = pauseValikko(self.SCREEN, self.WIDHT, self.HEIGHT, self.all_sprites)
                        jatka:bool = pause.valikko()
                        
                        if not jatka:
                            return
            
            for entity in self.all_sprites:
                self.SCREEN.blit(entity.surf, entity.rect)
            
            self.FramePerSec.tick(60)
            pygame.display.update()

            
    #Teen tähän valikon
    def valikko(self):
        pass


#Platform-luokka sandboxia varten
class platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (width/2, height - 10))
        self.counter = True

    #Metodi, joka vaihtaa platformin väriä
    def vaihdaVari(self):
        if self.counter:
            self.surf.fill((0,255,255))
            self.counter = False
        else:
            self.surf.fill((255,0,0))
            self.counter = True
