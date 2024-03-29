import pygame
from asetukset import vertical_tile_number, tile_size, screen_widht
from Kentta.tiles import AnimatedTile, StaticTile
from Kentta.support import import_folder
from random import choice, randint

#luodaan luokka tausta taivasta varten
class Sky:
    def __init__(self, horizon):
        self.top = pygame.image.load(
            'Kentta/graphics/decoration/sky/sky_top.png').convert()
        self.middle = pygame.image.load(
            'Kentta/graphics/decoration/sky/sky_middle.png').convert()
        self.bottom = pygame.image.load(
            'Kentta/graphics/decoration/sky/sky_bottom.png').convert()
        self.horizon = horizon

        # taivaan venytys
        self.top = pygame.transform.scale(self.top, (screen_widht, tile_size))
        self.middle = pygame.transform.scale(
            self.middle, (screen_widht, tile_size))
        self.bottom = pygame.transform.scale(
            self.bottom, (screen_widht, tile_size))

        # taivaan piirto
    def draw(self, surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horizon:
                surface.blit(self.top, (0, y))
            elif row == self.horizon:
                surface.blit(self.middle, (0, y))
            else:
                surface.blit(self.bottom, (0, y))

#luokka kentän pohjalla olevaa vettä varten 
class Water:
    def __init__(self, top, level_width):
        water_start = -screen_widht
        water_tile_width = 192
        tile_x_amount = int((level_width + screen_widht) / water_tile_width)
        self.water_sprites = pygame.sprite.Group()

        for tile in range(tile_x_amount):
            x = tile * water_tile_width + water_start
            y = top
            sprite = AnimatedTile(
                192, x, y, 'Kentta/graphics/decoration/water')
            self.water_sprites.add(sprite)

        # veden piirto pohjalle
    def draw(self, surface, shift):
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)

#luokka taustan pilviä varten
class Clouds:
    def __init__(self, horizon, level_widht, cloud_number):
        cloud_surf_list = import_folder('Kentta/graphics/decoration/clouds')
        min_x = -screen_widht
        max_x = level_widht + screen_widht
        min_y = 0
        max_y = horizon
        self.cloud_sprites = pygame.sprite.Group()
        
        #randomisoidaan pilvien määrää
        for cloud in range(cloud_number):
            cloud = choice(cloud_surf_list)
            x = randint(min_x, max_x)
            y = randint(min_y, max_y)
            sprite = StaticTile(0, x, y, cloud)
            self.cloud_sprites.add(sprite)

        # pilvien piirto
    def draw(self, surface, shift):
        self.cloud_sprites.update(shift)
        self.cloud_sprites.draw(surface)
