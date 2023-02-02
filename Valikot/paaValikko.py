import pygame, sys
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1260, 850))
pygame.display.set_caption("Menu")
BG = pygame.image.load("pics/Background.png") 


def get_font(size):
    return pygame.font.Font("pics/font.ttf", size)
    
def play():
    pygame.display.set_caption("Play")
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("black")
        
        PLAY_TEXT = get_font( 45).render("This is the play screen", True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT) 
        
        PLAY_BACK = Button(image= None, pos = (640, 460),
                           text_input = "BACK", font = get_font(45), base_color = "White", hovering_color = "Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    

        pygame.display.update()         
        
def options():
    pygame.display.set_caption("Options")
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("white")
        
        OPTIONS_TEXT = get_font(45).render("This is OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        OPTIONS_BACK = Button(image = None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        
def main_menu():
    pygame.display.set_caption("Menu")
    
    while True:
        SCREEN.blit(BG, (0 , 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        
        PLAY_BUTTON = Button(image=pygame.image.load("pics/Play Rect.png"), pos=(640, 250),
                             text_input = "PLAY", font = get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image = pygame.image.load("pics/Options Rect.png"), pos=(640, 400),
                                text_input = "OPTIONS", font = get_font(75), base_color="#d7fcd4", hovering_color = "White")
        QUIT_BUTTON = Button(image=pygame.image.load("pics/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font = get_font(75), base_color="#d7fcd4", hovering_color= "White")
        
        SCREEN.blit(MENU_TEXT,MENU_RECT)
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()
        
main_menu()           
