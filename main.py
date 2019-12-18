import pygame
import math
import random

# 20 x 20 grid 16 px
WIDTH = 20
HEIGHT = 20
CELL = 20

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
RED = (255, 20, 20)
GREEN = (20, 255, 20)

FPS = 20


def computer_move(gameboard):

    good_piece = False

    while not good_piece:
        x, y = random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1)

        if gameboard[x][y] == 'x':
            good_piece = True
            return x, y


def game_win(x,y, gameboard, player, other):

    if x - 2 >= 0 and x + 2 <= (WIDTH - 1) and y - 2 >= 0 and y + 2 <= (HEIGHT - 1):
        # Move is legal
        if gameboard[x - 1][y] == other:
            if gameboard[x - 2][y] == player:
                if gameboard[x - 1][y + 1] == player:
                    if gameboard[x - 1][y - 1] == player:

                        return True

        if gameboard[x + 1][y] == other:
            if gameboard[x + 2][y] == player:
                if gameboard[x + 1][y + 1] == player:
                    if gameboard[x + 1][y - 1] == player:

                        return True

        if gameboard[x][y - 1] == other:
            if gameboard[x][y - 2] == player:
                if gameboard[x - 1][y - 1] == player:
                    if gameboard[x + 1][y - 1] == player:

                        return True

        if gameboard[x][y + 1] == other:
            if gameboard[x][y + 2] == player:
                if gameboard[x - 1][y + 1] == player:
                    if gameboard[x + 1][y + 1] == player:

                        return True
    else:
        print("Bad move sherlock")


def show_bad_move(window):
    sm_font = pygame.font.Font('freesansbold.ttf', 12)

    bad = sm_font.render("Bad move", True, WHITE)
    bad_rect = bad.get_rect()
    bad_rect.center = (WIDTH * CELL / 2, HEIGHT * CELL / 2)

    window.blit(bad, bad_rect)
    pygame.display.update()
    pygame.time.delay(500)


def main():

    pygame.init()

    captured = 0

    window = pygame.display.set_mode((WIDTH * CELL, HEIGHT * CELL))
    pygame.display.set_caption("CAPUTRE!!!")
    clock = pygame.time.Clock()
    running = True
    show_game_over = False

    # initialize gameboard
    gameboard = [['x' for x in range(WIDTH)] for y in range(HEIGHT)]

    font = pygame.font.Font('freesansbold.ttf', 36)

    text = font.render('Game Over', True, WHITE, GREEN)

    text_rect = text.get_rect()
    text_rect.center = ((WIDTH * CELL) / 2, (HEIGHT * CELL) / 2)

    sm_font = pygame.font.Font('freesansbold.ttf', 12)

    x = 0
    y = 0

    player_moved = False

    player_cells = []
    comp_x = random.randint(1, WIDTH - 1)
    comp_y = random.randint(1, HEIGHT - 1)
    gameboard[comp_x][comp_y] = 'C'
    comp_cells = [(comp_x, comp_y)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = math.floor(x / CELL)
                y = math.floor(y / CELL)
                if not show_game_over:
                    if gameboard[x][y] == 'x':
                        gameboard[x][y] = 'P'
                        player_cells.append((x, y))
                        player_moved = True

                    else:
                        show_bad_move(window)
                    # player_cells.append((x, y))

        # Let's drop a random piece on the board
        while player_moved:
            comp_x, comp_y = computer_move(gameboard)
            if game_win(x, y, gameboard, 'P', 'C'):
                captured = captured + 1
                gameboard[comp_x][comp_y] = 'C'
                comp_cells.append((comp_x, comp_y))
                player_moved = False
            else:
                gameboard[comp_x][comp_y] = 'C'
                comp_cells.append((comp_x, comp_y))
                player_moved = False

        # Drawing
        score = sm_font.render('Player Score: ' + str(captured), True, WHITE)
        score_rect = score.get_rect()
        score_rect.center = (50, 10)

        if captured >= 10:
            show_game_over = True

        window.fill(BLACK)

        for item in comp_cells:
            pygame.draw.rect(window, RED, (item[0] * CELL, item[1] * CELL, CELL, CELL), 0)
        for item in player_cells:
            pygame.draw.rect(window, GREEN, (item[0] * CELL, item[1] * CELL, CELL, CELL), 0)

        for x in range(WIDTH):
            pygame.draw.line(window, GRAY, (x * CELL, 0), (x * CELL, HEIGHT * CELL))
        for y in range(HEIGHT):
            pygame.draw.line(window, GRAY, (0, y * CELL), (WIDTH * CELL, y * CELL))

        if show_game_over:
            window.blit(text, text_rect)
            pygame.display.update()
            # pygame.time.delay(2000)

        window.blit(score, score_rect)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()