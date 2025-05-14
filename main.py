import pygame
import enemy
import bullet
from player import Player
from bullet import Bullet
from enemy import Enemy
from utils import check_collision
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
heart_img = pygame.image.load("assets/heart.png").convert_alpha()
heart_img = pygame.transform.scale(heart_img, (24, 24))


enemy.enemy_images = [
    pygame.transform.scale(pygame.image.load("assets/enemy1.png").convert_alpha(), (75, 75)),
    pygame.transform.scale(pygame.image.load("assets/enemy2.png").convert_alpha(), (75, 75))
]
# Tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet.bullet_image = pygame.image.load("assets/bullet.png").convert_alpha()
background = pygame.image.load("assets/background1.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Fontes
font = pygame.font.SysFont("Arial", 24)
button_font = pygame.font.SysFont("Arial", 30)

# Função para reiniciar o jogo
def reset_game():
    global bullets, enemies, score, game_over, enemy_spawn_timer, lives
    bullets = []
    enemies = []
    score = 0
    enemy_spawn_timer = 0
    game_over = False
    lives = 3

# Inicializações
player = Player(WIDTH // 2, HEIGHT - 60)
bullets = []
enemies = []
enemy_spawn_delay = 60
enemy_spawn_timer = 0
lives = 3
score = 0
game_over = False

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        player.move(keys)

        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append(Bullet(player.x, player.y))

        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_delay:
            enemies.append(Enemy())
            enemy_spawn_timer = 0

        for bullet in bullets[:]:
            bullet.move()
            if bullet.off_screen():
                bullets.remove(bullet)

        for enemy in enemies[:]:
            enemy.move()

            player_rect = pygame.Rect(player.x - player.width // 2, player.y, player.width, player.height)
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            if player_rect.colliderect(enemy_rect):
                enemies.remove(enemy)
                lives -= 1
                if lives <= 0:
                    game_over = True

            if enemy.off_screen():
                enemies.remove(enemy)
                continue

            for bullet in bullets[:]:
                if check_collision(bullet.x, bullet.y, bullet.radius, enemy.x, enemy.y, enemy.width, enemy.height):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
                    break

    screen.blit(background, (0, 0))
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    score_text = font.render(f"Pontos: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    for i in range(lives):
        screen.blit(heart_img, (WIDTH - (i + 1) * 30, 10))

    if game_over:
        go_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, HEIGHT // 2 - 60))

        button_text = button_font.render("JOGAR NOVAMENTE", True, (0, 0, 0))
        button_rect = pygame.Rect(WIDTH // 2 - 130, HEIGHT // 2, 350, 50)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                reset_game()

    pygame.display.flip()

pygame.quit()
