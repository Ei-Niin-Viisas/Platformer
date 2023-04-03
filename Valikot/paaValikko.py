import sys, pygame
from Valikot.button import Button

#Luodaan luokka/olio päävalikolle
class paaValikko:    
    #olion konstruktori
    def __init__(self, width, height):
        self.SCREEN = pygame.display.get_surface()
        self.WIDTH = width
        self.HEIGHT = height
        self.BG = pygame.image.load("pics/Background.png") 
        pygame.display.set_caption("Menu")

        self.lukko = pygame.time.Clock()

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
                        #self.play()
                        return
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            
            self.lukko.tick(60)  
            pygame.display.update()
        

