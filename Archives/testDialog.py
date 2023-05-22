import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()


# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NPC Dialog Box")


bg_image = pygame.image.load('../beavUp/assets/bg.png').convert_alpha()

# Define colors
BLACK = (0, 0, 0)
WHITE = (0, 0, 0)

# Define font
font = pygame.font.SysFont("Arial", 20)

# Define the NPC class
class NPC:
    def __init__(self, x, y, message, options=None):
        self.x = x
        self.y = y
        self.message = message
        self.options = options
        self.dialog_box = DialogBox()

    def display_question_mark(self):
        # Draw the question mark box above the NPC's head
        pygame.draw.rect(screen, WHITE, (self.x, self.y - 30, 30, 30))
        question_mark = font.render("?", True, BLACK)
        screen.blit(question_mark, (self.x + 10, self.y - 25))

    def start_dialog(self):
        self.dialog_box.display(self.message, self.options)
        print(self.message)
        if not self.options:
            # Hide the dialog box and revert to a question mark
            self.dialog_box = None
            
# Define the DialogBox class
class DialogBox:
    def __init__(self):
        self.x = 100
        self.y = screen_height - 150
        self.width = screen_width - 200
        self.height = 100
        self.text_x = self.x + 10
        self.text_y = self.y + 10
        self.text_width = self.width - 20
        self.text_height = self.height - 20

    def display(self, message, options=None):
        print("displayed!")
        # Draw the dialog box
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, WHITE, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        
        # Render the text
        lines = self.wrap_text(message)
        print("This is wrapped: " + str(lines))
        
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (230, 230, 230))
            screen.blit(text_surface, (self.text_x, self.text_y + i * 20))
            #print(line)
            text = font.render(line, True, BLACK)

        # Display response options
        if options:
            response_y = self.y + self.height + 10
            for i, option in enumerate(options):
                option_text = font.render(f"{i+1}. {option}", True, BLACK)
                screen.blit(option_text, (self.text_x, response_y + i * 20))
                


    def wrap_text(self, message):
        # Wrap the text to fit within the dialog box
        words = message.split()
        lines = []
        current_line = words[0]
        for word in words[1:]:
            if font.size(current_line + ' ' + word)[0] < self.text_width:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        return lines

# Create an instance of the NPC
#npc = NPC(400, 300, "Hello! How are you?")
npc = NPC(400, 300, "Hello! How are you? I'm fantastic, I love unicorns, cats, and cherries!", ["I'm good!", "Not too bad.", "Could be better."])


# Main game loop
running = True
dialog = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Check if the player clicked on the question mark
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] >= npc.x and mouse_pos[0] <= npc.x + 30 and mouse_pos[1] >= npc.y - 30 and mouse_pos[1] <= npc.y:
                npc.start_dialog()
                print("clicked")
                dialog = True
            elif npc.dialog_box:
                # Check if the player clicked on a response option
                for i, option in enumerate(npc.options):
                    if mouse_pos[0] >= npc.dialog_box.text_x and mouse_pos[0] <= npc.dialog_box.text_x + npc.dialog_box.text_width and mouse_pos[1] >= npc.dialog_box.y + npc.dialog_box.height + 10 + i * 20 and mouse_pos[1] <= npc.dialog_box.y + npc.dialog_box.height + 30 + i * 20:
                        print(f"Player chose option {i+1}: {option}")
                        # Update the game state based on the chosen option
                        print("woof")
                        # Hide the dialog box and revert to a question mark
                        npc.dialog_box = None
                        break

    # Clear the screen
    screen.fill((255, 255, 255))
    #Set Background Screen
    #screen.blit(bg_image, (0, 0))

    if dialog == True:
        text = font.render(npc.message, True, BLACK)
        text_rect = text.get_rect(center=(50 + 100 // 2, 50 + 100 // 2))
        screen.blit(text, text_rect)
                
    # Draw the NPC
    npc.display_question_mark()

    # Update the display
    pygame.display.update()

# Quit the game
