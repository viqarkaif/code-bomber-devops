# src/map.py

import pygame
from player import Player
from bomb import Bomb

class GameMap:
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.grid_size = 20
        self.map = [[0] * (self.width // self.grid_size) for _ in range(self.height // self.grid_size)]
        self.player = Player(100, 100, (0, 255, 0))  # Starting at position (100, 100)
        self.bombs = []

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Black background

        # Drawing the grid
        for row in range(0, self.height, self.grid_size):
            for col in range(0, self.width, self.grid_size):
                pygame.draw.rect(screen, (255, 255, 255), (col, row, self.grid_size, self.grid_size), 1)

        self.player.draw(screen)

        # Draw bombs
        for bomb in self.bombs:
            bomb.draw(screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move("UP")
                elif event.key == pygame.K_s:
                    self.player.move("DOWN")
                elif event.key == pygame.K_a:
                    self.player.move("LEFT")
                elif event.key == pygame.K_d:
                    self.player.move("RIGHT")
                elif event.key == pygame.K_SPACE:  # Space to place a bomb
                    self.bombs.append(Bomb(self.player.x + 15, self.player.y + 15))
