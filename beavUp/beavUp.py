import pygame, sys
from settings import *
from level import Level
import requests
import gpt

pygame.init()
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('beavUp')
clock = pygame.time.Clock()
level = Level(level_map, screen)


# load images
# beavy_image = pygame.image.load('assets/beavy.png').convert_alpha()
bg_image = pygame.image.load('assets/bg.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    screen.blit(bg_image, (0, 0))

    pygame.display.update()
    clock.tick(60)
