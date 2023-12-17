import pygame
from random import randint
from copy import deepcopy

time_stopped = False
stop_counter = 10
Width = 1300
Height = 700
Tile = 15
W, H = (Width // Tile), (Height // Tile)

clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((Width, Height))

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

label = pygame.font.Font('fonts1/Roboto-BlackItalic.ttf', 40)
random_label = label.render('Randomly generated', False, (0, 0, 0))
handle_label = label.render('Put cells yourself', False, (0, 0, 0))
handle_label_rect = handle_label.get_rect(topleft=(200, 250))
random_label_rect = random_label.get_rect(topleft=(700, 250))

gameplay1 = False
gameplay2 = False
current_state = [[0 for i in range(W)] for j in range(H)]

drawing_mode = False

def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1
    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                time_stopped = not time_stopped
    clock.tick(10)
    if gameplay1:
        screen.fill(pygame.Color('white'))

        [pygame.draw.line(screen, pygame.Color('black'), (x, 0), (x, Height)) for x in range(0, Width, Tile)]
        [pygame.draw.line(screen, pygame.Color('black'), (0, y), (Width, y)) for y in range(0, Height, Tile)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_state[y][x]:
                    pygame.draw.rect(screen, pygame.Color('red'),
                                     (x * Tile + 2, y * Tile + 2, Tile - 2, Tile - 2))
                if not time_stopped:
                    next_field[y][x] = check_cell(current_state, x, y)
        if not time_stopped:
            current_state = deepcopy(next_field)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        if mouse and pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            current_state[y // Tile][x // Tile] = 1
    elif gameplay2:
        screen.fill(pygame.Color('white'))

        [pygame.draw.line(screen, pygame.Color('black'), (x, 0), (x, Height)) for x in range(0, Width, Tile)]
        [pygame.draw.line(screen, pygame.Color('black'), (0, y), (Width, y)) for y in range(0, Height, Tile)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(screen, pygame.Color('red'), (x * Tile + 2, y * Tile + 2, Tile - 2, Tile - 2))
                if not time_stopped:
                    next_field[y][x] = check_cell(current_field, x, y)
        if not time_stopped:
            current_field = deepcopy(next_field)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        if mouse and pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            current_field[y // Tile][x // Tile] = 1
    else:
        screen.fill((49, 226, 220))
        screen.blit(random_label, random_label_rect)
        screen.blit(handle_label, handle_label_rect)

        mouse = pygame.mouse.get_pos()
        if random_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay2 = True

        if handle_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay1 = True


    pygame.display.update()
