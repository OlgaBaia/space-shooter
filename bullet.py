import pygame

bullet_image = None  # Será carregado no main.py

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(bullet_image, (10, 20))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def off_screen(self):
        return self.rect.bottom < 0

    @property
    def x(self):
        return self.rect.centerx

    @property
    def y(self):
        return self.rect.centery

    @property
    def radius(self):
        return self.rect.width // 2
