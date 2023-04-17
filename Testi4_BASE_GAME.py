<<<<<<< HEAD
# TUTORIAL:
# https://www.youtube.com/watch?v=AY9MnQ4x3zk

import pygame
import sys
import math
from Testi4_settings import *
=======
import pygame
import sys
import math
from Testi4_methods import *
from random import randint
import random




def display_score(play_time):
    current_time = pygame.time.get_ticks() - play_time
    score_surf = font.render(str(current_time), False, "Black")
    score_rect = score_surf.get_rect(center = (WINDOW_WIDTH/2, 40))
    screen.blit(score_surf, score_rect)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= randint(3, 10)

            screen.blit(demoEnemy_surface, obstacle_rect)

        return obstacle_list
    else:
        return []
>>>>>>> origin/Juuso

pygame.init()
pygame.display.set_caption("Game")

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
fps = 60

<<<<<<< HEAD
running = True
=======


player = pygame.sprite.GroupSingle()
player.add(Player())

>>>>>>> origin/Juuso

font = pygame.font.Font("pics/font.ttf", 30)

sky_surface = pygame.image.load("pics/Background.png").convert()
ground_surface = pygame.image.load("pics/Background2.png").convert()
<<<<<<< HEAD
text_surface = font.render("Score: ", False, "Black")

=======
ground_rect= ground_surface.get_rect(topleft = (0,500))

# text_surface = font.render("Score: ", False, "Black")
# text_rect = text_surface.get_rect(center = (WINDOW_WIDTH/2, 40))

# Obstacles
>>>>>>> origin/Juuso
demo_Enemy_surface = pygame.image.load("pics/green_little_bug.png").convert_alpha()
demoEnemy_surface = pygame.transform.scale(demo_Enemy_surface, (50,40))
demoEnemy_rect = demoEnemy_surface.get_rect(midbottom = (600,500))

<<<<<<< HEAD
player1_surface = pygame.image.load("pics/player/frame_1.png").convert_alpha()
player_surface = pygame.transform.scale(player1_surface, (50,40))
player_rect = player_surface.get_rect(midbottom = (50, 500))

def main():
    
    # Handle events
    while running:
=======



# player1_surface = pygame.image.load("pics/player/frame_1.png").convert_alpha()
# player_surface = pygame.transform.scale(player1_surface, (50,40))
# player_rect = player_surface.get_rect(midbottom = (50, 500))






# luodaan vihollis-oliot
viholliset = []
for i in range(10):
    x = random.randint(0, WINDOW_WIDTH-50)
    y = random.randint(50, WINDOW_HEIGHT-50)
    # x= 200
    # y= 300
    width = 50
    height = 40
    speed = random.randint(1, 5)
    distance = (x, x + random.randint(100, 300)) # tuple, jolla aloitus ja loppupiste
    image_path = "pics/green_little_bug.png"
    vihollinen = Vihollinen(x, y, width, height, speed, distance, image_path)
    viholliset.append(vihollinen)



def main():
    # Timer
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1000)

    game_running = True
    play_time = 0
    

    # Handle events
    while True:
>>>>>>> origin/Juuso
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
            
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
=======
            if game_running:
                # Koordinaatit hiirellä
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse pressed at: " + str(event.pos))
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE and player_rect.bottom == 500:
                #         #if player_jumpCount > 0:
                #             player_gravity = -20
                #             #player_jumpCount -= 1

                #     if player_rect.bottom == 500:
                #         #if player_rect.colliderect(ground_rect):
                #         print("collision with ground")
                #         #player_jumpCount = 1


                    # huono implementaatio
                    # if event.key == pygame.K_a:
                    #     print("A pressed")
                    #     player_rect.x -= 5

                    # if event.key == pygame.K_d:
                    #     print("D pressed")
                    #     player_rect.x += 5


                # if event.type == obstacle_timer:
                #     obstacle_rect_list.append(demoEnemy_surface.get_rect(bottomright = ((randint(WINDOW_WIDTH, WINDOW_WIDTH+500)),500)))



            # else:
            #     if event.type == pygame.KEYDOWN:
            #         game_running = True
            #         demoEnemy_rect.left = WINDOW_WIDTH
            #         play_time = pygame.time.get_ticks()
                    


        if game_running:     
            screen.blit(sky_surface,(0,0)) # (surface joka lisätään display surfacen päälle,(position x,y))
            screen.blit(ground_surface, ground_rect)
            #screen.blit(text_surface,text_rect)
            #display_score(play_time)


            # demoEnemy_rect.left -= 3
            # if demoEnemy_rect.right <= 0:
            #     demoEnemy_rect.left += WINDOW_WIDTH

            # screen.blit(demoEnemy_surface,demoEnemy_rect)



            # Player
            # player_gravity += 1
            # player_rect.y += player_gravity
            # if player_rect.bottom > 500:
            #     player_rect.bottom = 500
            # screen.blit(player_surface, player_rect)
            
            player.draw(screen)
            player.update()

            # Obstacle movement
            #obstacle_rect_list = obstacle_movement(obstacle_rect_list)
            # liikuta ja piirrä kaikki viholliset
            for vihollinen in viholliset:
                vihollinen.move()
                vihollinen.draw(screen)

            # Game over
            # if demoEnemy_rect.colliderect(player_rect):
            #     game_running = False
                # pygame.quit()
                # exit()


            # if player_rect.colliderect(demoEnemy_rect):
            #     print("collision")
            
            # mouse_pos = pygame.mouse.get_pos()
            # mouse_press = pygame.mouse.get_pressed()
            # if player_rect.collidepoint(mouse_pos):
            #     print("collision")
                
            # if mouse_press != (False, False, False):
            #     print(mouse_press)
            

            
            # Drawing logic
            pygame.display.update()
            clock.tick(fps)
        
>>>>>>> origin/Juuso
        
    
        
        
        
        
        
if __name__ == "__main__":
    main()