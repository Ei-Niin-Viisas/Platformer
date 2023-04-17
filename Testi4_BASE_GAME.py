# TUTORIAL:
# https://www.youtube.com/watch?v=AY9MnQ4x3zk

import pygame
import sys
import math
from Testi4_settings import *

pygame.init()
pygame.display.set_caption("Game")

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
fps = 60

running = True

font = pygame.font.Font("pics/font.ttf", 30)

sky_surface = pygame.image.load("pics/Background.png").convert()
ground_surface = pygame.image.load("pics/Background2.png").convert()
text_surface = font.render("Score: ", False, "Black")

demo_Enemy_surface = pygame.image.load("pics/green_little_bug.png").convert_alpha()
demoEnemy_surface = pygame.transform.scale(demo_Enemy_surface, (50,40))
demoEnemy_rect = demoEnemy_surface.get_rect(midbottom = (600,500))

player1_surface = pygame.image.load("pics/player/frame_1.png").convert_alpha()
player_surface = pygame.transform.scale(player1_surface, (50,40))
player_rect = player_surface.get_rect(midbottom = (50, 500))

def main():
    
    # Handle events
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
            
        screen.blit(sky_surface,(0,0)) # (surface joka lisätään display surfacen päälle,(position x,y))
        screen.blit(ground_surface,(0,500))
        screen.blit(text_surface,(300,50))
        
        demoEnemy_rect.left -= 3
        if demoEnemy_rect.right <= 0:
            demoEnemy_rect.left += 800

        screen.blit(demoEnemy_surface,demoEnemy_rect)
        
        screen.blit(player_surface, player_rect)
        
        # demo_enemy_1_movement()
        
        
        # Drawing logic
        pygame.display.update()
        clock.tick(fps)
        
        
def demo_enemy_1_movement():
    demoEnemy_x_def_pos = 600
    demoEnemy_y_def_pos = 460
    
    
    
    demoEnemy_x_pos = demoEnemy_x_def_pos - 3
    demoEnemy_y_pos = demoEnemy_y_def_pos
    screen.blit(demoEnemy_surface,(demoEnemy_x_pos, demoEnemy_y_pos))
    # if demoEnemy_x_pos > 1:
    #     demoEnemy_x_pos -= 40
    #     print("pos reduced")
    # else:
    #     demoEnemy_x_pos += 40
    #     print("pos increased")
        
    
        
        
        
        
        
if __name__ == "__main__":
    main()