import pygame
from tiles import Tile
from settings import tile_size, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from npc import Npc

class Level:
    def __init__(self, level_data, surface):
        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.npcs = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'N':
                    npc_sprite = Npc((x, y))
                    self.npcs.add(npc_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH // 4 and direction_x < 0:
            self.world_shift_x = 5
            player.speed = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH // 4) and direction_x > 0:
            self.world_shift_x = -5
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 5

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < SCREEN_HEIGHT // 2 and direction_y < 0:
            self.world_shift_y = 5
            player.speed = 0
        elif player_y > SCREEN_HEIGHT - (SCREEN_HEIGHT // 2) and direction_y > 0:
            self.world_shift_y = -5
            player.speed = 0
        else:
            self.world_shift_y = 0
            player.speed = 5

    def horizontal_move_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_move_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.is_on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


    def run(self):
        #level tiles
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.scroll_y()

        #npc
        self.npcs.update(self.world_shift_x, self.world_shift_y)
        self.vertical_move_collision()
        self.horizontal_move_collision()
        self.npcs.draw(self.display_surface)

        #player
        self.player.update()
        self.vertical_move_collision()
        self.horizontal_move_collision()
        self.player.draw(self.display_surface)
