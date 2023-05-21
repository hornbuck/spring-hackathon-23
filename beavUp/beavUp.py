import pygame, sys
from settings import *
from level import Level
import requests
import gpt

# Initialize Pygame
pygame.mixer.init()
pygame.init()
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('beavUp')
clock = pygame.time.Clock()
level = Level(level_map, screen)

# Load the music file: You can change file path if you download from link above from your device
pygame.mixer.music.load("assets/bgmusic.mp3")

# Play the music in an infinite loop
pygame.mixer.music.play(loops=-1)

# load images
bg_image = pygame.image.load('assets/bg.png').convert_alpha()
#gpt.newImage('Make a pixel style background of mountains in the far distance', 'assets/bg.png') #AI-generated image

# Runs the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    screen.fill('black')
    screen.blit(bg_image, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)