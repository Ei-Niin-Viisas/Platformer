import pygame
from random import randint

class Gravity:
    def gravity(self, player):
        player.gravity = 0


class Vihollinen():

    def __init__(self, x, y, width, height, speed, distance, image_path):
        #self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.distance = distance
        self.direction = 1 #1 = oikealle, -1 = vasemmalle
        self.image_path = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image_path, (width, height))
        self.rect = self.image.get_rect(midbottom = (x, y))

    def move(self):
        self.rect.move_ip(self.speed * self.direction, 0)

        if self.rect.left < self.distance[0]: # distance tuplen x0 -koordinaatti
            self.direction = 1
        elif self.rect.right > self.distance[1]: #distance tuplen x1 -koordinaatti
            self.direction = -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)







class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Liitä tähän eri pelaaja-framet

        self.def_image = pygame.image.load("pics/player/frame_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.def_image, (50,40))

        self.rect = self.image.get_rect(midbottom = (80,500))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 500:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500

    def update(self):
        self.player_input()
        self.apply_gravity()