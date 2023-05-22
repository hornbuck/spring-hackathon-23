import pygame

# Loads sprite images
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
beavy_image = pygame.image.load('assets/beavy.png').convert_alpha()
beavy_opp = pygame.image.load('assets/beavy_opp.png').convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = pygame.transform.scale(beavy_image, (55, 55))
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.4
        self.jump_speed = -12
        self.is_on_ground = False

    def import_char_assets(self):
        character_path = '/assets/beavy.png'

    def get_input(self):
        keys = pygame.key.get_pressed()

        #Changes direction
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            #Sprite change
            self.image = pygame.transform.scale(beavy_image, (55, 55))
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #Sprite change
            self.image = pygame.transform.scale(beavy_opp, (55, 55))
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

        if not self.is_on_ground:
            self.is_on_ground = False

    def jump(self):
        if self.is_on_ground:
            self.direction.y = self.jump_speed
            self.is_on_ground = False

    def update(self):
        self.get_input()
        self.apply_gravity()
