import pygame, random
from pygame.locals import *

from collections import deque

from math import floor

def random_grid_position():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (floor(x) * 10, floor(y) * 10)

def colision(c1, c2):
    return c1 == c2

def colision_wall(x, y, width, height):
    return not (0 <= x < width and 0 <= y < height)

def get_direction(event):
    global keymap
    return keymap[event.key] if event.key in keymap else None

def update_snake_movement(direction):
    x, y = snake[0]
    ix, iy = direction
    snake[0] = (x + ix, y + iy)

def draw_snake_movement():
    snake.appendleft(snake[0])
    snake.pop()

UP = (0, -10)
DOWN = (0, 10)
LEFT = (-10, 0)
RIGHT = (10, 0)

keymap = {
    K_UP: UP,
    K_RIGHT: RIGHT,
    K_DOWN: DOWN,
    K_LEFT: LEFT
}

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = deque([(200, 200), (210, 200), (220,200)])

snake_piece = pygame.Surface((10, 10))
snake_piece.fill((255, 255, 255))

apple = pygame.Surface((10, 10))
apple.fill((255,0,0))
apple_pos = random_grid_position()

direcao = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            direcao = get_direction(event)
            
    if colision(snake[0], apple_pos):
        apple_pos = random_grid_position()
        snake.append((0, 0))

    if colision_wall(snake[0][0], snake[0][1], 600, 600):
        pygame.quit()

    for i in range(1, len(snake)):
        if colision(snake[0], snake[i]):
            pygame.quit()

    draw_snake_movement()
    update_snake_movement(direcao)
    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_piece, pos)
    
    pygame.display.update()
