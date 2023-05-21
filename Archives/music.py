# Author: Aadil Ali
# Script to loop music
# download link for mp3 file: https://downloads.khinsider.com/game-soundtracks/album/pokemon-emerald-enhanced-soundtrack/1-04%2520Introductions.mp3

import pygame

# Initialize Pygame
pygame.mixer.init()
pygame.init()

# Set the display size (optional, I do not know the resolution for the pygame file so this is a default size)
pygame.display.set_mode((800, 600))

# Load the music file: You can change file path if you download from link above from your device
pygame.mixer.music.load("/Users/aadi1_a1i/Downloads/music/bgmusic.mp3")

# Play the music in an infinite loop
pygame.mixer.music.play(loops=-1)

# Wait for the music to finish playing
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
