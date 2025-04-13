
# src/main.py
# main.py
print("This is a change!")

import pygame
import sys
from map import GameMap

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman DevOps Game!")

# Game Map
game_map = GameMap(WIDTH, HEIGHT)

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Handle player input and game logic
    game_map.handle_events(events)
    
    # Draw everything
    game_map.draw(screen)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit the game properly
pygame.quit()
sys.exit()

