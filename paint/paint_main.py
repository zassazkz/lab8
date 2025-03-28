import pygame
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Использование встроенных цветов Pygame
colors = ['red', 'green', 'blue']
color = 'black'
background_color = 'white'

screen.fill(background_color)
pygame.display.flip()

# Функция для рисования кнопок выбора цвета
def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index * 40, 0, 40, 40))

# Функция выбора цвета
def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return 'red'
        elif 40 < x <= 80 and 0 <= y <= 40:
            return 'green'
        elif 80 < x <= 120 and 0 <= y <= 40:
            return 'blue'
    return color

# Функция рисования
mode = 'circle'
erasing = False  # Флаг режима стирания

def painting(color, mode):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), 27)
        elif mode == 'rect':
            pygame.draw.rect(screen, color, (x, y, 40, 40), 4)
        elif mode == 'eraser':
            pygame.draw.circle(screen, background_color, (x, y), 20)

# Отображение текста
font = pygame.freetype.SysFont("Arial", 24)
def draw_text(text, position, color):
    font.render_to(screen, position, text, color)

draw_text("E: Eraser", (10, 40), 'black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                mode = 'eraser'
        elif event.type == pygame.MOUSEBUTTONDOWN and mode == 'eraser':
            erasing = True
        elif event.type == pygame.MOUSEBUTTONUP and mode == 'eraser':
            erasing = False
    
    for i in range(len(colors)):
        draw_rect(i)

    color = pick_color()
    if erasing:
        painting(background_color, 'eraser')
    else:
        painting(color, mode)

    clock.tick(60)
    pygame.display.update()