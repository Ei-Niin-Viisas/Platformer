import pygame
from support import import_csv_layout, import_cut_graphics
from asetukset import tile_size, screen_height
from tiles import Tile, StaticTile, Crate, Coin, Palm
from enemy import Enemy
from decorations import Sky, Water, Clouds
from player import Player
from particles import ParticleEffect


class Level:
    def __init__(self, level_data, surface):
        # perus setuppi
        self.display_surface = surface
        self.world_shift = 0

        # pleieri
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # terrain setuppi
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(
            terrain_layout, 'terrain')

        # graassi setuppi
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        # laatikot
        crates_layout = import_csv_layout(level_data['crates'])
        self.crate_sprites = self.create_tile_group(crates_layout, 'crates')

        # koliket
        coin_layout = import_csv_layout(level_data['coins'])
        self.coin_sprites = self.create_tile_group(coin_layout, 'coins')

        # foreground palmut
        fg_palm_layout = import_csv_layout(level_data['fg palms'])
        self.fg_palm_sprites = self.create_tile_group(
            fg_palm_layout, 'fg palms')

        # takapajulan palmut
        bg_palm_layout = import_csv_layout(level_data['bg palms'])
        self.bg_palm_sprites = self.create_tile_group(
            bg_palm_layout, 'bg palms')

        # vihulaaset
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # rajotukset
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(
            constraint_layout, 'constraints')

        # Decos
        self.sky = Sky(8)
        level_widht = len(terrain_layout[0]) * tile_size
        self.Water = Water(screen_height - 40, level_widht)
        self.clouds = Clouds(400, level_widht, 8)

    def create_tile_group(self, layout, type):

        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    # chekataan mitä tuodaan ja piirrteään
                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics(
                            'Kentta/graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'grass':
                        grass_tile_list = import_cut_graphics(
                            'Kentta/graphics/decoration/grass/grass.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)

                    if type == 'coins':
                        if val == '0':
                            sprite = Coin(tile_size, x, y,
                                          'Kentta/graphics/coins/gold')
                        if val == '1':
                            sprite = Coin(tile_size, x, y,
                                          'Kentta/graphics/coins/silver')

                    if type == 'fg palms':
                        if val == '0':
                            sprite = Palm(
                                tile_size, x, y, 'Kentta/graphics/terrain/palm_small', 38)
                        if val == '1':
                            sprite = Palm(
                                tile_size, x, y, 'Kentta/graphics/terrain/palm_large', 64)

                    if type == 'bg palms':
                        sprite = Palm(tile_size, x, y,
                                      'Kentta/graphics/terrain/palm_bg', 64)

                    if type == 'enemies':
                        sprite = Enemy(tile_size, x, y)

                    if type == 'constraints':
                        sprite = Tile(tile_size, x, y)

                    sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface,
                                    self.create_jump_particles)
                    self.player.add(sprite)
                if val == '1':
                    hat_surface = pygame.image.load(
                        'Kentta/graphics/character/hat.png').convert_alpha()
                    sprite = StaticTile(tile_size, x, y, hat_surface)
                    self.goal.add(sprite)

    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def create_jump_particles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collide_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + \
            self.fg_palm_sprites.sprites()
        for sprite in collide_sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collide_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + \
            self.fg_palm_sprites.sprites()
        for sprite in collide_sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < o or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def run(self):
        # run the entire game/level

        # taivas
        self.sky.draw(self.display_surface)
        self.clouds.draw(self.display_surface, self.world_shift)

        # takapajulan palmut
        self.bg_palm_sprites.update(self.world_shift)
        self.bg_palm_sprites.draw(self.display_surface)

        # terraini
        self.terrain_sprites.update(self.world_shift)
        self.terrain_sprites.draw(self.display_surface)

        # vihut
        self.enemy_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)

        # lootat
        self.crate_sprites.update(self.world_shift)
        self.crate_sprites.draw(self.display_surface)

        # ruohua
        self.grass_sprites.update(self.world_shift)
        self.grass_sprites.draw(self.display_surface)

        # koliket
        self.coin_sprites.update(self.world_shift)
        self.coin_sprites.draw(self.display_surface)

        # etualan palmuja
        self.fg_palm_sprites.update(self.world_shift)
        self.fg_palm_sprites.draw(self.display_surface)

        # pelaaja spraitit
        self.player.update()
        # self.horizontal_movement_collision()
        # self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        # vesi pohjalle
        self.Water.draw(self.display_surface, self.world_shift)
