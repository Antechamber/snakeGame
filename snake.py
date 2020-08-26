import sys
import pygame
import time
import random

pygame.init()

# display controls
dis_width = 800
dis_height = 600
snake_color = (0, 0, 0)
food_color = (0, 0, 255)
red = (200, 0, 0)
background = (0, 150, 150)
score_color = (0, 0, 0)
font_style = pygame.font.SysFont(None, 35)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()


# message
def message(msg: str, color: tuple):
    mesg = font_style.render(msg, True, color)
    location = [round(dis_width / 3), round(dis_height / 3)]
    dis.blit(mesg, location)


def display_score(score: int):
    location = [0, 0]
    dis.blit(font_style.render("Score: " + str(score), True, score_color), location)


def display_snake(snake_block: int, snake_list: tuple):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])


def game_loop():
    game_over = False
    game_close = False

    score = 0

    # gameplay controls
    x1 = dis_width / 2
    y1 = dis_height / 2
    x_change = 0
    y_change = 0
    snake_block = 10
    snake_speed = 30

    snake_list = []
    snake_length = 1
    foodx = round(random.randrange(1, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(1, dis_height - snake_block) / 10) * 10

    while not game_over:
        # game exit / reset options
        while game_close:
            dis.fill(background)
            display_score(score)
            message("You lost, dork... Q - quit, N - new game", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = False
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_n:
                        game_loop()
        # keystrokes -> snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (y_change <= 0 or snake_length == 1):
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN and (y_change >= 0 or snake_length == 1):
                    x_change = 0
                    y_change = snake_block
                elif event.key == pygame.K_LEFT and (x_change <= 0 or snake_length == 1):
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT and (x_change >= 0 or snake_length == 1):
                    x_change = snake_block
                    y_change = 0
        # hitting the border
        if x1 == 0 or y1 == 0 or x1 >= dis_width or y1 >= dis_height:
            game_close = True

        x1 += x_change
        y1 += y_change
        dis.fill(background)

        # draw snake
        pygame.draw.rect(dis, snake_color, [round(x1), round(y1), snake_block, snake_block])
        snake_head = []
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del(snake_list[0])

        # hitting snake body
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        display_snake(snake_block, snake_list)

        # food generation / eating check
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        if x1 == foodx and y1 == foody:
            score += 1
            snake_length += 1
            foodx = round(random.randrange(1, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(1, dis_height - snake_block) / 10) * 10

        display_score(score)
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


game_loop()
