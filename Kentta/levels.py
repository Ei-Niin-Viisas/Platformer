import pygame
from Kentta.support import import_csv_layout, import_cut_graphics
from asetukset import tile_size, screen_height, screen_widht
from Kentta.tiles import Tile, StaticTile, Crate, Coin, Palm
from Hahmot.enemy import Enemy
from Kentta.decorations import Sky, Water, Clouds
from Hahmot.player import Player
from Hahmot.particles import ParticleEffect


class Level:
    def __init__(self, level_data, surface):
        # perus setuppi
        self.display_surface = pygame.display.get_surface()
        self.world_shift = -2
        self.pistelaskuri = 0

        # pleieri
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()

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
        self.oletusFontti = pygame.font.Font("pics/font.ttf", 15)
        self.laskuri = self.oletusFontti.render('kolikot: 0' , True , "black")
        self.pisteet = self.laskuri.get_rect(topright = (screen_widht -40, 40))


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

    # ruudun liikutus pelaajan mukaan
    def scroll_with_player(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        suunta_x = player.direction.x
        
        # Kun pelaaja liikkuu tiettyyn pisteeseen asti,
        # sen sijaan että liikutettaisiin pelaajaa,
        # liikutetaankin ympäröivää maailmaa vastakkaiseen
        # suuntaan


        # Kun liikutaan vasemmalle
        if player_x < screen_widht / 2.5 and suunta_x < 0:
            self.world_shift = 6
            player.speed = 0
        # Ja oikealle
        elif player_x > screen_widht - (screen_widht / 2.5) and suunta_x > 0:
            self.world_shift = -6
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def osumat(self):
        pelaaja:Player = self.player.sprite
        #Vihu tappaa pelaajan
        for vihu in self.enemy_sprites:
            if pygame.sprite.collide_rect(pelaaja, vihu):
                if pelaaja.rect.bottom <= vihu.rect.top + 12:
                    vihu.kill()
                    pelaaja.jump()
                else:
                    return 1
            
        #Pelaaja kerää kolikon
        for kolikko in self.coin_sprites:
            if pygame.sprite.collide_rect(pelaaja, kolikko):
                kolikko.kill()
                self.pistelaskuri += 1
                self.laskuri = self.oletusFontti.render('kolikot: ' + str(self.pistelaskuri) , True , "black")
                print(self.pistelaskuri)

        #Pelaaja tippuu rotkoon ja kuolee
        if pelaaja.rect.top > pygame.display.get_window_size()[1]:
            return 1
        
        #Pelaaja osuu hattuun ja voittaa pelin
        if pygame.sprite.collide_rect(pelaaja, self.goal.sprite):
            return 2
    
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
        pelaaja:Player = self.player.sprite
        osumat:list = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()
        pelaaja.fysiikat(osumat)
    

        osuttu:int = self.osumat()
        if osuttu != None:
            return osuttu
        
        self.display_surface.blit(self.laskuri, self.pisteet)
            
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)

        self.scroll_with_player()

        # vesi pohjalle
        self.Water.draw(self.display_surface, self.world_shift)
