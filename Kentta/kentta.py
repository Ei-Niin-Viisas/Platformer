import pygame, sys, time
from pygame.locals import *
from Valikot.peliValikko import pauseValikko
from threading import Thread
from Kentta.ui import ui
from Hahmot.Player import player

#Luokka 
class taso:
    #Tähän tason luonti sitten, kun se on tehty
    #def __init__(self, taso:list, player):
    #    pass

    #Sandboxin konstruktori
    def __init__(self):
        self.SCREEN = pygame.display.get_surface()
        self.WIDTH, self.HEIGHT  = pygame.display.get_window_size()
        self.PT1 = platform(self.WIDTH, self.HEIGHT)
        self.PLAYER = player()
        self.UI = ui(self.PT1, self.SCREEN)
        
        #t = Thread(target=self.UI.paivitaUI, args=())
        #t.setDaemon(True)
        #t.start()

        self.all_sprites = pygame.sprite.Group()
        self.alustat = pygame.sprite.Group()
        self.all_sprites.add(self.PT1)
        self.alustat.add(self.PT1)
        self.all_sprites.add(self.PLAYER)
        self.FramePerSec = pygame.time.Clock()

    #Testi-metodi, joka piirtää punaisen "lattian"
    def testi(self):
        pygame.display.set_caption("Peli")
        self.SCREEN.fill((0,0,0))
        pygame.display.flip()

        while True:
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_ESCAPE:
                        pause = pauseValikko(self.SCREEN, self.WIDTH, self.HEIGHT)
                        jatka:bool = pause.valikko()
                        self.SCREEN.fill((0,0,0))
                        pygame.display.flip()
                        
                        if not jatka:
                            return
                        
                    #elif event.key == pygame.K_SPACE:
                    #    self.PLAYER.jump(self.alustat)

            tausta = self.SCREEN.fill((0,0,0))
            #self.all_sprites.add(tausta)

            self.PLAYER.move(self.alustat)

            piirto = []
            piirto.append(tausta)


            for entity in self.all_sprites:
                self.SCREEN.blit(entity.surf, entity.rect)
                piirto.append(entity.rect)
            
            #pygame.sprite.LayeredUpdates.change_layer(self.PT1,1)

            self.FramePerSec.tick(60)
            pygame.display.update(piirto)


#Platform-luokka sandboxia varten
class platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (width/2, height - 10))
        self.counter = 0

    #Metodi, joka vaihtaa platformin väriä
    def vaihdaVari(self):
        if self.counter%2 == 0:
            self.surf.fill((0,255,255))
            self.counter += 1
        else:
            self.surf.fill((255,0,0))
            self.counter += 1

    def naytaLaskuri(self):
        #print(self.counter)
        pass
