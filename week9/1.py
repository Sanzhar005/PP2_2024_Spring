import pygame
from datetime import datetime

# pygame initialization
pygame.init()
screen = pygame.display.set_mode((650, 450))
window_title = pygame.display.set_caption("mickey mouse clock")
icon = pygame.display.set_icon(pygame.image.load(r"C:\Users\sanch\Downloads\mickeyclock.jpg"))
clock = pygame.time.Clock()

# loading the images 
bg_surf = pygame.image.load(r"C:\Users\sanch\Downloads\mickeyclock.jpg")
leftarm_surf = pygame.image.load(r"C:\Users\sanch\Downloads\leftarm1.png")
rightarm_surf = pygame.image.load(r"C:\Users\sanch\Downloads\rightarm1.png")
bg_rect = bg_surf.get_rect(center = (325, 225))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pygame.transform.rotate(leftarm_surf, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(rightarm_surf, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)

    screen.blit(bg_surf, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pygame.display.flip()
    clock.tick(60)