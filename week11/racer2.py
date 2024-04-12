import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coin2 = 0
# настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\sanch\Downloads\AnimatedStreet (1).png")

# создаем белый экран
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# фоновый звук
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)  # i use -1 to loop the music

# создаем группу спрайтов врага
class Enemy(pygame.sprite.Sprite):
    # конструкция
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\sanch\Downloads\Enemy (1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    # метод перемещения
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# создаем группу спрайтов игрока
class Player(pygame.sprite.Sprite):
    # конструкция
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\sanch\Downloads\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    # метод перемещения
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# создаем группу спрайтов монет
class Coin(pygame.sprite.Sprite):
    # конструкция
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\sanch\Downloads\free-icon-dollar-coin-9787486.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

class BigCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            r"C:\Users\sanch\Downloads\free-icon-dollar-coin-9787486-fotor-2024030511740.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.move_ip(0, SPEED)

# настройка спрайтов
P1 = Player()
E1 = Enemy()
C1 = Coin()
B1 = BigCoin()

# создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

big_coins = pygame.sprite.Group()
big_coins.add(B1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, C1, B1, E1)

# добавление нового пользовательского события
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    counter = font_small.render(str(coin2), True, BLACK)
    DISPLAYSURF.blit(counter, (380, 10))

    # проверка на столкновение с монетами
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        coin2 += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        new_coin.rect.top = 0
        new_coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        if coin2 % 10 == 0:
            SPEED += 1
            new_coin = BigCoin()
            big_coins.add(new_coin)
            all_sprites.add(new_coin)
            new_coin.rect.top = 0
            new_coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    big_coins_collided = pygame.sprite.spritecollide(P1, big_coins, True)
    for big_coin in big_coins_collided:
        coin2 += 5
        big_coin.kill()

    # перемещение и перерисовывание всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # запускается если происходит столкновение между игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\sanch\Downloads\crash.mp3").play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)