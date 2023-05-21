# Author: Aadil Ali
# Sample script to initiate dialogue during race between 4 of the sprites

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Race Competition")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load sprite images
sprite_images = [
    pygame.image.load("sprite1.png"),
    pygame.image.load("sprite2.png"),
    pygame.image.load("sprite3.png"),
    pygame.image.load("sprite4.png")
]

# Set up sprites
num_sprites = 4
sprites = []
sprite_positions = []
sprite_speeds = []
sprite_width = 50
sprite_height = 50
start_y = screen_height - sprite_height

for i in range(num_sprites):
    sprite = sprite_images[i]
    sprite_rect = sprite.get_rect()
    sprite_rect.x = 0
    sprite_rect.y = start_y - (sprite_height * i)
    sprites.append(sprite)
    sprite_positions.append(sprite_rect)
    sprite_speeds.append(random.randint(1, 4))

# Set up the flag
flag_image = pygame.image.load("flag.png")
flag_rect = flag_image.get_rect()
flag_rect.x = screen_width - sprite_width
flag_rect.y = 0

# Set up the dialogue box
dialogue_box_width = 300
dialogue_box_height = 150
dialogue_box_x = (screen_width - dialogue_box_width) // 2
dialogue_box_y = (screen_height - dialogue_box_height) // 2
dialogue_box = pygame.Rect(dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height)

# Set up the font
font = pygame.font.Font(None, 24)

# Game loop
running = True
finished = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not finished:
        screen.fill(BLACK)

        # Move the sprites
        for i in range(num_sprites):
            sprite_positions[i].x += sprite_speeds[i]

            # Check if the sprite has reached the flag
            if sprite_positions[i].colliderect(flag_rect):
                finished = True
                winner = i + 1

        # Draw the sprites
        for i in range(num_sprites):
            screen.blit(sprites[i], sprite_positions[i])

        # Draw the flag
        screen.blit(flag_image, flag_rect)

    # Draw the dialogue box
    pygame.draw.rect(screen, WHITE, dialogue_box)
    
    # Render text in the dialogue box
    if finished:
        text = font.render(f"Race Finished! Winner: Sprite {winner}", True, BLACK)
    else:
        text = font.render("Race in progress...", True, BLACK)
    
    text_rect = text.get_rect(center=(dialogue_box.x + dialogue_box.width // 2, dialogue_box.y + dialogue_box.height // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

# Clean up
pygame.quit()
