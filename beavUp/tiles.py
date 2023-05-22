import pygame

# Loads sprite images
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
platform_image = pygame.image.load('assets/platform.png').convert_alpha()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill((255, 255, 255))
        self.image = pygame.transform.scale(platform_image, (55, 55))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift
