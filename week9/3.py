import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x, y = WIDTH // 2, HEIGHT // 2

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - 20 >= radius:
                    y -= 20
            elif event.key == pygame.K_DOWN:
                if y + 20 <= HEIGHT - radius:
                    y += 20
            elif event.key == pygame.K_LEFT:
                if x - 20 >= radius:
                    x -= 20
            elif event.key == pygame.K_RIGHT:
                if x + 20 <= WIDTH - radius:
                    x += 20

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()