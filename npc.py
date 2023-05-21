import pygame

class Npc(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.4
        self.jump_speed = -12
        self.is_on_ground = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        self.is_on_ground = False

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift
