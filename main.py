import pygame

from scripts.player import Player
from scripts.bullet import Bullet
from scripts.functions import load_image

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()

FPS = 60

background = load_image('images\\background.png', (800, 600), None)
enemy_image = load_image('images\\enemy.png', (30, 30), (0, 0, 0))
bullet_image = load_image('images\\bullet.png', ())
player_image = load_image('images\\player.png')

player_image = pygame.transform.scale(player_image, (75, 75))
player = Player(400, 550, player_image, 5)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.key == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.append(
                    Bullet(player.rect.centerx, player.rect.y, bullet_image, 10)
                )

    player.update()
    for bullet in bullets.copy():
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullet.remove(bullet)

    window.blit(background, (0, 0))
    player.render(window)
    for bullet in bullets:
        bullet.render(window)
    pygame.display.update()
    clock.tick(FPS)