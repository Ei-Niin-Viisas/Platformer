import sys, pygame
from Valikot.button import Button

class pauseValikko(pygame.sprite.Sprite):

    def __init__(self, screen, width, height):
        super().__init__()
        self.SCREEN = screen
        self.width = width/2
        self.height = height/2


    def valikko(self):
        # white color 
        color = (255,255,255) 
        # light shade of the button 
        color_light = (170,170,170) 
        # dark shade of the button 
        color_dark = (100,100,100) 
        # defining a font 
        smallfont = pygame.font.SysFont('Corbel',35) 
        
        # rendering a text written in 
        # this font 
        text1 = smallfont.render('Continue' , True , color)
        text2 = smallfont.render('Quit to menu' , True , color) 
        
        while True: 
            
            for ev in pygame.event.get(): 
                
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                    
                #checks if a mouse is clicked 
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    
                    #if the mouse is clicked on the 
                    # button the game is terminated 
                    if self.width-150 <= mouse[0] <= self.width+300 and self.height/1.5 <= mouse[1] <= self.height/1.5+40: 
                        return True
                    if self.width-150 <= mouse[0] <= self.width+300 and self.height/1.5+200 <= mouse[1] <= self.height/1.5+240: 
                        return False
                
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        return True
                    

            # täyttää nelikulmion värillä
            nelikulmio = pygame.draw.rect(self.SCREEN,"blue",[self.width/2,self.height/2,self.width,self.height])
            
            #self.rect = self.surf.get_rect(center = (self.width/2, self.height - 10))

            # stores the (x,y) coordinates into 
            # the variable as a tuple 
            mouse = pygame.mouse.get_pos() 
            
            # if mouse is hovered on a button it 
            # changes to lighter shade 
            if self.width-150 <= mouse[0] <= self.width+300 and self.height/1.5 <= mouse[1] <= self.height/1.5+40: 
                pygame.draw.rect(self.SCREEN,color_light,[self.width-150,self.height/1.5,300,40]) 
                
            else: 
                pygame.draw.rect(self.SCREEN,color_dark,[self.width-150,self.height/1.5,300,40])

            if self.width-150 <= mouse[0] <= self.width+300 and self.height/1.5+200 <= mouse[1] <= self.height/1.5+240: 
                pygame.draw.rect(self.SCREEN,color_light,[self.width-150,self.height/1.5+200,300,40])       
            else: 
                pygame.draw.rect(self.SCREEN,color_dark,[self.width-150,self.height/1.5+200,300,40]) 
            
            # superimposing the text onto our button 
            self.SCREEN.blit(text1, (self.width-100, self.height/1.5))
            self.SCREEN.blit(text2, (self.width-100, self.height/1.5+200)) 
            
            # updates the frames of the game 
            pygame.display.update(nelikulmio)