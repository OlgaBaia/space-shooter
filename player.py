import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))  # ajusta tamanho
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    @property
    def x(self):
        return self.rect.centerx

    @property
    def y(self):
        return self.rect.top

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height
