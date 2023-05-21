import pygame
duck_image = pygame.image.load('assets/betterduck.png').convert_alpha()
lion_image = pygame.image.load('assets/mount_lion.png').convert_alpha()
turtle_image = pygame.image.load('assets/turtle.png').convert_alpha()


class Npc(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.transform.scale(duck_image, (100, 100))
        self.rect = self.image.get_rect(topleft=pos)

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

class Lion(Npc):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.transform.scale(lion_image, (110, 100))

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.4
        self.jump_speed = -12
        self.is_on_ground = False

class Turtle(Npc):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.transform.scale(turtle_image, (100, 100))

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.4
        self.jump_speed = -12
        self.is_on_ground = False
