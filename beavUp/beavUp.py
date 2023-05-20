import pygame, sys
import gpt
import requests

pygame.init()
clock = pygame.time.Clock()

# Game Screen Info.
screen_width = 1024
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('beavUp')

# load images
beavy_image = pygame.image.load('assets/beavy.png').convert_alpha()
#ImageGen: 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

gpt.newImage('down a mountain in Oregon', 'assets/bg.png') #AI-generated image


bg_image = pygame.image.load('assets/bg.png').convert_alpha()

# Floor dimensions
floor_height = screen_height // 6
floor_y = screen_height - floor_height
floor_color = (0, 255, 0)


class Player:
    def __init__(self, x, y, width, height, speed, jump_height, color):
        self.image = pygame.transform.scale(beavy_image, (150, 150))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.jump_height = jump_height
        self.color = color
        self.is_jumping = False

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  # move left
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:  # move right
            self.x += self.speed
        if not self.is_jumping:
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]: #activate jump
                self.is_jumping = True
                self.jump_counter = self.jump_height

    def do_jump(self):
        if self.is_jumping:
            self.y -= self.jump_counter
            self.jump_counter -= 1
            if self.jump_counter < -self.jump_height:
                self.is_jumping = False
                self.y = floor_y - self.height

    def draw(self, surface):
            #Displays a cube
            #pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

            #Displays the sprite image
            screen.blit(self.image, (self.x, self.y))

# Create Player
player = Player(screen_width // 2, floor_y - 50, 100, 50, 5, 15, (255, 255, 255))
player.y = floor_y - player.height

#Generate Platforms

#Create NPCs
#coug_phrase = gpt.dialogue("cougar", "Billy Bob", "hungry and annoyed")
#duck_phrase = gpt.dialogue("duck", "Dr. Quack", "silly, tired, and anxious")
#turtle_phrase = gpt.dialogue("mutant turtle", "Donatello", "funny, hungry, and feeling purple")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle player actions
    player.handle_keys()
    player.do_jump()

    # player boundaries
    if player.x < 0:
        player.x = 0
    if player.x > screen_width - player.width:
        player.x = screen_width - player.width
    if player.y < 0:
        player.y = 0
    if player.y > floor_y - player.height:
        player.y = floor_y - player.height

    # fill screen
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, 0))
    pygame.draw.rect(screen, floor_color, pygame.Rect(0, floor_y, screen_width, floor_height))
    
    # draw player
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)
