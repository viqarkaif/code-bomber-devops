
# src/bomb.py

import pygame
import time

class Bomb:
    def __init__(self, x, y, color=(255, 0, 0), radius=20, delay=3):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.delay = delay
        self.start_time = time.time()
        self.exploded = False

    def is_exploded(self):
        # Check if enough time has passed
        return time.time() - self.start_time >= self.delay

    def draw(self, screen):
        if not self.is_exploded():
            # Draw the bomb as a red circle
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        else:
            # Draw explosion as a big orange blast
            pygame.draw.circle(screen, (255, 165, 0), (self.x, self.y), self.radius * 2)
