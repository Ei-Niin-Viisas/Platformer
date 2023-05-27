import pygame, sys, time
from pygame.locals import *
from Valikot.peliValikko import pauseValikko
from threading import Thread
from Kentta.levels import Level
from Kentta.game_data import kentat

#Luokka 
class taso:

    #Luokan konstruktori
    def __init__(self):
        self.SCREEN = pygame.display.get_surface()
        self.WIDTH, self.HEIGHT  = pygame.display.get_window_size()
        self.levels = None
        self.FPSlukko = pygame.time.Clock()


    #Testi-metodi, joka saa kentän numeron ja alkaa pyörittää silmukkaa, jossa kenttää päivitetään.
    def aja(self, indeksi):
        pygame.display.set_caption("Peli")
        pygame.display.flip()

        #Käynnistää musiikin
        pygame.mixer.init()
        taustamusiikki = pygame.mixer.Sound("music/BTD6.mp3")
        taustamusiikki.play()

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
            #tai näytää voitto ruudun maaliin osuttaessa.
            if osuttu == 1:
                self.SCREEN.fill((0,0,0))
                
                smallfont = pygame.font.Font("pics/font.ttf", 75)
                text1 = smallfont.render('YOU DIED' , True , "red")
                text1_rect = text1.get_rect(center = (self.WIDTH/2, self.HEIGHT/2))
                self.SCREEN.blit(text1, text1_rect)
                pygame.display.flip()
                time.sleep(2)
                taustamusiikki.stop()
                return
            elif osuttu == 2:
                self.SCREEN.fill("white")
                smallfont = pygame.font.Font("pics/font.ttf", 75)
                text1 = smallfont.render('YOU WIN' , True , "blue")
                text1_rect = text1.get_rect(center = (self.WIDTH/2, self.HEIGHT/2))
                self.SCREEN.blit(text1, text1_rect)
                pygame.display.flip()
                time.sleep(2)
                taustamusiikki.stop()
                return

            
            self.FPSlukko.tick(60)
            pygame.display.flip()
