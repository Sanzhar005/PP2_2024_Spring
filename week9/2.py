import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Music player")

playlist = [
    r"C:\Users\sanch\Downloads\Miyagi & Эндшпиль feat. Рем Дигга - I Got Love.mp3",
    r"C:\Users\sanch\Downloads\Қайрат Нұртас & Нюша - Алматы тун.mp3",
    r"C:\Users\sanch\Downloads\Hiro - Любимые два часа.mp3"
]

current_track = 0

playing = False
paused = False

pygame.mixer.music.load(playlist[current_track])

def toggle_pause():
    global playing, paused
    if playing and not paused:
        pygame.mixer.music.pause()
        paused = True
    elif paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.play()
        playing = True

controls = {
    pygame.K_SPACE: lambda: toggle_pause(),
    pygame.K_s: lambda: pygame.mixer.music.stop(),
    pygame.K_n: lambda: next_track(),
    pygame.K_p: lambda: prev_track()
}

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in controls:
                controls[event.key]()

    screen.fill((255, 255, 255))

    track_text = os.path.basename(playlist[current_track])
    font = pygame.font.Font(None, 36)
    text_surface = font.render(track_text, True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
