import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#Floor dimensions
floor_height = screen_height // 6
floor_y = screen_height - floor_height
floor_color = (0, 255, 0)

#Block Dimensions
block_width = 50
block_height = 50

#block position
block_x = screen_width // 2
block_y = floor_y - block_height
block_speed = 5
jump_height = 15
block_color = (255, 255, 255)

is_jumping = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Detect Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: #move left
        block_x -= block_speed
    if keys[pygame.K_RIGHT]: #move right
        block_x += block_speed

    #Block can only jump when it is NOT already jumping
    if not is_jumping:
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            is_jumping = True
            jump_counter = jump_height

    #jumping
    if is_jumping:
        block_y -= jump_counter
        jump_counter -= 1

        if jump_counter < -jump_height:
            is_jumping = False
            block_y = floor_y - block_height

    #block boundaries
    if block_x < 0:
        block_x = 0
    if block_x > screen_width - block_width:
        block_x = screen_width - block_width
    if block_y < 0:
        block_y = 0
    if block_y > floor_y - block_height:
        block_y = floor_y - block_height

    # fill screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, floor_color, pygame.Rect(0, floor_y, screen_width, floor_height))
    pygame.draw.rect(screen, block_color, pygame.Rect(block_x, block_y, block_width, block_height))

    pygame.display.flip()
    clock.tick(60)