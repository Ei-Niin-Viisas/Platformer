import pygame
from Kentta.tiles import AnimatedTile
from random import randint
from Hahmot.player import Player


class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'Kentta/graphics/enemy/run')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(1, 3)

    def move(self):
        self.rect.x += self.speed

    #spriten kääntö
    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    #vihujen suunnan muutto
    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()


