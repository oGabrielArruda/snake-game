import pygame, random
from pygame.locals import *

def random_grid_position():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return(x//10 * 10, y//10 * 10)

def colisao(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def getDirection(event):
    if event.key == K_UP:
        key = UP
    if event.key == K_RIGHT:
        key = RIGHT
    if event.key == K_DOWN:
        key = DOWN
    if event.key == K_LEFT:
        key = LEFT
    return key
        

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 4

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]

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
            direcao = getDirection(event)
            
    if colisao(snake[0], apple_pos):
        apple_pos = random_grid_position()
        snake.append((0, 0))

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        pygame.quit()

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()            

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direcao == UP:
        snake[0] = ((snake[0][0], snake[0][1]-10))
    if direcao == DOWN:
        snake[0] = ((snake[0][0], snake[0][1]+10))
    if direcao == RIGHT:
        snake[0] = ((snake[0][0]+10, snake[0][1]))
    if direcao == LEFT:
        snake[0] = ((snake[0][0]-10, snake[0][1]))


    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_piece, pos)
    
    pygame.display.update()
