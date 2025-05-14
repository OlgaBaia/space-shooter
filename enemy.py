import pygame
import random

# Pré-carrega as imagens (fora da classe, para não duplicar carregamentos)
enemy_images = []

class Enemy:
    def __init__(self):
        self.image = random.choice(enemy_images)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, 800 - self.width)
        self.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def off_screen(self):
        return self.y > 600
