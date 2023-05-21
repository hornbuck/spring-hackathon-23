import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((0, 255, 255))
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

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        self.is_on_ground = False

    def jump(self):
        if self.is_on_ground:
            self.direction.y = self.jump_speed

    def update(self):
        self.get_input()