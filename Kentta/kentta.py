import pygame, sys, time
from pygame.locals import *
from Valikot.peliValikko import pauseValikko
from threading import Thread
from Kentta.ui import ui
from Kentta.kolikot import Kolikko
from Hahmot.Player_vanha import player
from Kentta.levels import Level
from Kentta.game_data import kentat

#Luokka 
class taso:
    #Tähän tason luonti sitten, kun se on tehty
    #def __init__(self, taso:list, player):
    #    pass

    #Sandboxin konstruktori
    def __init__(self):
        self.SCREEN = pygame.display.get_surface()
        self.WIDTH, self.HEIGHT  = pygame.display.get_window_size()


        #self.UI = ui(self.PT1, self.SCREEN)
        self.levels = None
        
        #t = Thread(target=self.UI.paivitaUI, args=())
        #t.setDaemon(True)
        #t.start()

        self.FPSlukko = pygame.time.Clock()

    #Testi-metodi, joka piirtää punaisen "lattian"
    def aja(self, indeksi):
        pygame.display.set_caption("Peli")
        pygame.display.flip()

        #kolikko = Kolikko(200, 500)
        #self.all_sprites.add(kolikko)
        self.levels = Level(kentat[indeksi], self.SCREEN)

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
                        

            #Jos pelaajaan on kentässä osuttu, muuttuja saa arvon True
            osuttu:int = self.levels.run()

            #If-lause, joka näyttää kuolemaruudun ja heittää pelaajan päävalikkoon
            if osuttu == 1:
                self.SCREEN.fill((0,0,0))
                smallfont = pygame.font.SysFont('Corbel',70) 
                text1 = smallfont.render('Kualit huano!!!' , True , "red")
                self.SCREEN.blit(text1, (self.WIDTH/3, self.HEIGHT/2))
                pygame.display.flip()
                time.sleep(2)
                return
            elif osuttu == 2:
                self.SCREEN.fill("white")
                smallfont = pygame.font.SysFont('Corbel',70) 
                text1 = smallfont.render('Voitit kentän!!!' , True , "blue")
                self.SCREEN.blit(text1, (self.WIDTH/3, self.HEIGHT/2))
                pygame.display.flip()
                time.sleep(2)
                return

            
            self.FPSlukko.tick(60)
            pygame.display.flip()


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
