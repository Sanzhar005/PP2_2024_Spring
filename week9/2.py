import pygame
import os

# Инициализация Pygame и звуковой системы
pygame.init()

# Создание окна
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Музыкальный проигрыватель")

# Загрузка аудиофайлов
playlist = [
    r"C:\Users\sanch\Downloads\V_X_V_PRiNCE_-_Asylym_66964833.mp3",
    r"C:\Users\sanch\Downloads\Kajjrat_Nurtas_Nyusha_-_Almaty_Tn_64400710.mp3",
    r"C:\Users\sanch\Downloads\Azis_-_Sen_Trope_63175699.mp3"
]

# Текущий трек
current_track = 0

# Флаги для управления воспроизведением
playing = False
paused = False

# Загрузка первого трека
pygame.mixer.music.load(playlist[current_track])

# Словарь клавиш управления
controls = {
    pygame.K_SPACE: lambda: pygame.mixer.music.pause() if playing and not paused else pygame.mixer.music.unpause() if paused else pygame.mixer.music.play(),
    pygame.K_s: lambda: pygame.mixer.music.stop(),
    pygame.K_n: lambda: next_track(),
    pygame.K_p: lambda: prev_track()
}

# Функция переключения на следующий трек
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

# Функция переключения на предыдущий трек
def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

# Основной цикл программы
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

    # Отображение информации о текущем треке
    track_text = os.path.basename(playlist[current_track])
    font = pygame.font.Font(None, 36)
    text_surface = font.render(track_text, True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(30)

# Выход из Pygame
pygame.quit()