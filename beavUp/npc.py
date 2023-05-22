import pygame
import time
    
class Npc(pygame.sprite.Sprite):
        
    def __init__(self, pos, texture, screen):
        super().__init__()
        self.image = pygame.transform.scale(texture, (100, 100))

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

    def print_dialogue(self, screen, width, height, message, speaker):
        #The code below is completely generated by OpenAI's ChatGPT,
        #unless otherwise indicated.

        # Define colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        #Screen parameters - added by human
        screen_width = width
        screen_height = height

        #Renders speaker
        screen.blit(speaker, (height - 200, width // 4)) #added by a human


        # Define colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        # Define font and font size
        font_name = "Arial"
        font_size = 20
        font = pygame.font.SysFont(font_name, font_size)

        # Define the multiline string
        #changed by a human
        multiline_string = message

        # Calculate the line width and height
        line_width = screen_width // 5 #changed by a human
        line_height = font_size + 5  # Add some extra padding between lines

        def split_multiline_string(string): #changed by a human
            
            
            words = string.split(",") #changed by a human
                    
            return words
            #human code ends here

        def calculate_text_position(lines):
            total_height = len(lines) * line_height
            y = (screen_height - total_height) // 2
            return y

        def display_multiline_text(lines):
            y = calculate_text_position(lines)
            
            for i, line in enumerate(lines):
                #line += ","
                text_surface = font.render(line, True, BLACK)
                x = (screen_width - line_width) // 4 #changed by a human
                screen.blit(text_surface, (x + 400, (y + i * line_height) + 75))
                

        # Split the multiline string into lines
        lines = split_multiline_string(multiline_string) #changed by a human


        # Display the multiline text
        display_multiline_text(lines)


        ##END OF AI CODE

        
