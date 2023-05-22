import pygame
from tiles import Tile
from settings import tile_size, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from npc import Npc
import gpt

# Loads sprite images
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
turtle = pygame.image.load('assets/turtle.png').convert_alpha()
cougar = pygame.image.load('assets/mountain lion.png').convert_alpha()
duck = pygame.image.load('assets/betterduck.png').convert_alpha()

# Load dialog images
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
turtle_speaker = pygame.image.load('assets/turtle_talk.png').convert_alpha()

#AI Phrase Generation
turtle_phrase = gpt.dialogue("mutant turtle", "Donatello", "funny, hungry, and feeling purple")
#turtle_phrase = "Time to moooove, up the mountain!!!"
        
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

                #Turtle Sprite
                if cell == 'T':
                    self.turtle_npc = Npc((x, y), turtle, screen)
                    self.npcs.add(self.turtle_npc)
                    
                    
                #Cougar Sprite
                if cell == 'C':
                    self.cougar_npc = Npc((x, y), cougar, screen)
                    self.npcs.add(self.cougar_npc)
                    #AI Phrase Generation
                    #coug_phrase = gpt.dialogue("cougar", "Billy Bob", "hungry and annoyed")

                #Duck Sprite
                if cell == 'D':
                    self.duck_npc = Npc((x, y), duck, screen)
                    self.npcs.add(self.duck_npc)
                    #AI Phrase Generation
                    #duck_phrase = gpt.dialogue("duck", "Dr. Quack", "silly, tired, and anxious")
                    

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

        #npc-dialogue
        self.turtle_npc.print_dialogue(screen, SCREEN_WIDTH, SCREEN_HEIGHT, turtle_phrase, turtle_speaker)


        #player
        self.player.update()
        self.vertical_move_collision()
        self.horizontal_move_collision()
        self.player.draw(self.display_surface)
