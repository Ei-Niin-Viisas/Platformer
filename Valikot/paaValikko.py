import sys, pygame
from Valikot.button import Button
#import pygame_menu

#Luodaan luokka/olio päävalikolle
class paaValikko:    
    #olion konstruktori
    def __init__(self, width, height):
        self.SCREEN = pygame.display.get_surface()
        self.WIDTH = width
        self.HEIGHT = height
        self.BG = pygame.image.load("pics/Background.png") 
        pygame.display.set_caption("Menu")

    def get_font(self, size):
        return pygame.font.Font("pics/font.ttf", size)
    
    def play(self):
        pygame.display.set_caption("Play")
        palaa:bool = False


        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

        
            self.SCREEN.fill("black")
            
            PLAY_TEXT = self.get_font(45).render("This is the play screen", True, "white")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(self.WIDTH/2, 260))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT) 
            
            
            
            PLAY_BACK = Button(image= None, pos = (self.WIDTH/2, 460),
                            text_input = "BACK", font = self.get_font(45), base_color = "White", hovering_color = "Green")
            
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        #self.main_menu()
                        palaa = True
                        
            pygame.display.update()

            if PLAY_MOUSE_POS.checkForInput(pygame.mouse.get_pos()):
                self.ask_level()

            if palaa:
                break  
        
    def options(self):
        pygame.display.set_caption("Options")
        palaa = False
        
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            
            self.SCREEN.fill("white")
            
            OPTIONS_TEXT = self.get_font(45).render("This is OPTIONS screen.", True, "black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(self.WIDTH/2, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            
            OPTIONS_BACK = Button(image = None, pos=(self.WIDTH/2, 460),
                                text_input="back", font=self.get_font(75), base_color="black", hovering_color="Green")
        
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        #self.main_menu()
                        palaa = True

            pygame.display.update()
            if palaa:
                break

    def main_menu(self):
        
        while True:
            pygame.display.set_caption("Menu")
            self.SCREEN.blit(self.BG, (0 , 0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(self.WIDTH/2, self.HEIGHT/2-250))
            
            PLAY_BUTTON = Button(image=pygame.image.load("pics/Play Rect.png"), pos=(self.WIDTH/2, self.HEIGHT/2-100),
                                text_input = "PLAY", font = self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image = pygame.image.load("pics/Options Rect.png"), pos=(self.WIDTH/2, self.HEIGHT/2+100),
                                    text_input = "OPTIONS", font = self.get_font(75), base_color="#d7fcd4", hovering_color = "White")
            QUIT_BUTTON = Button(image=pygame.image.load("pics/Quit Rect.png"), pos=(self.WIDTH/2, self.HEIGHT/2+250),
                                text_input="QUIT", font = self.get_font(75), base_color="#d7fcd4", hovering_color= "White")
            
            self.SCREEN.blit(MENU_TEXT,MENU_RECT)
            
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        chosen_level = self.choose_level()
                        return chosen_level
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    
            pygame.display.update()


    def choose_level(self):
        level_list = [0,1]
        apullista = []
        nappilista = []
        
        selected_level = None
        self.SCREEN.fill("black")


        for i in level_list:
                level_name =  "level" + str(i)
                level_text = self.get_font(45).render(f"{i+1}. {level_name}", True, "white")
                level_rect = level_text.get_rect(center=(self.WIDTH/4, 260 + i*100))

                level_button = Button(image=None, pos=((self.WIDTH*3)/4, 260 + i*100),
                    text_input="SELECT", font=self.get_font(45), base_color="White", hovering_color="Green")
                
                apullista.append((level_text, level_rect))
                nappilista.append(level_button)

        while selected_level is None:

            for i in range(len(apullista)):
                self.SCREEN.blit(apullista[i][0], apullista[i][1])
                level_button = nappilista[i]

                level_button.changeColor(pygame.mouse.get_pos())
                level_button.update(self.SCREEN)
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for nappi in range(len(nappilista)):
                            if nappilista[nappi].checkForInput(pygame.mouse.get_pos()):
                                selected_level = nappi
        
            pygame.display.update()
        
        return selected_level

