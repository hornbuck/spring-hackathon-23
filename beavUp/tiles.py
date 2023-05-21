import pygame

# Loads sprite images
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
flag_image = pygame.image.load('assets/platform.png').convert_alpha()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((55, 45))
        self.image.fill((0, 0, 0, 0))
        self.image.set_colorkey((0, 0, 0, 0))

        flag = self.image = pygame.transform.scale(flag_image, (55, 45))
        self.image.blit(flag, (0, -30))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift