# src/player.py

import pygame

class Player:
    def __init__(self, x, y, color, speed=1):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = 30
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, direction):
        if direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed
        elif direction == "LEFT":
            self.x -= self.speed
        elif direction == "RIGHT":
            self.x += self.speed
        
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
