import pygame
import math
import random
from play.comp_brain import *

#PALLET
WHITE = (255, 255, 255)
RED   = (255,  20,  20)
BLACK = (  0,   0,   0)
GREEN = ( 20, 255,  20)


def capture_piece(gameboard, posx, posy, turn):
    # print(str(len(gameboard)) + " : " + str(len(gameboard[0])))

    if turn == "player":
        attacker = 1
        pawn = 2
    else:
        attacker = 2
        pawn = 1

    captured = 0,0
    if posx - 2 > 0 and posy - 2 > 0:
        if posx + 2 < 24 and posy + 2 < 17:
            # north
            if gameboard[posx][posy - 1] == pawn:
                # make sure that we're still on the board
                if posy - 2 > 0:
                    # lastly we need to see if the point at + 2 is our piece
                    if gameboard[posx][posy - 2] == attacker:
                            captured = posx, posy - 1
            # south
            elif gameboard[posx][posy + 1] == pawn:
                if posy + 2 < 17:
                    if gameboard[posx][posy + 2] == attacker:
                        captured = posx, posy + 1
            #east
            elif gameboard[posx + 1][posy] == pawn:
                if posx + 2 < 24:
                    if gameboard[posx + 2][posy] == attacker:
                        captured = posx + 1, posy
            #west
            elif gameboard[posx - 1][posy] == pawn:
                if posx - 2 > 0:
                    if gameboard[posx - 2][posy] == attacker:
                        captured = posx - 1, posy
            #northeast
            elif gameboard[posx + 1][posy - 1] == pawn:
                if posx + 2 < 24 and posy - 2 > 0:
                    if gameboard[posx + 2][posy - 2] == attacker: 
                        caputred = posx + 1, posy - 1
            #southeast
            elif gameboard[posx + 1][posy + 1] == pawn:
                if posx + 2 < 24 and posy + 2 < 17:
                    if gameboard[posx + 2][posy + 2] == attacker: 
                        captured = posx + 1, posy + 1
            #southwest
            elif gameboard[posx - 1][posy + 1] == pawn:
                if posx - 2 > 0 and posy + 2 < 17:
                    if gameboard[posx - 2][posy + 2] == attacker: 
                        captured = posx - 1, posy + 1
            #northwest
            elif gameboard[posx - 1][posy - 1] == pawn:
                if posx - 2 > 0 and posy - 2 > 0:
                    if gameboard[posx - 2][posy - 2] == attacker: 
                        captured = posx - 1, posy - 1
            else:
                caputred = -1, -1
        else:
            captured = -1, -1
    else:
        captured = -1, -1

    return captured

def main():

    pygame.init()
    window = pygame.display.set_mode((800,576))
    pygame.display.set_caption("Squares")

    clock = pygame.time.Clock()
    FPS = 60

    WIDTH = 25
    HEIGHT = 18
    # let's paint a grid that 32x32 pixels per square 25 * 18
    gameboard = [ [0 for x in range(HEIGHT)] for y in range(WIDTH)]
    
    running  = True
    
    mousex,mousey = 0,0
    
    comp_brain = Bot(0)

    while running: 
        
        left = False
        right = False
        comp_turn = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousex, mousey = pygame.mouse.get_pos()
                    left = True
                    comp_turn = True
                    # print (str(mousex) + " : " + str(mousey))
                if event.button == 3:
                    mousex, mousey = pygame.mouse.get_pos()
                    right =True


        # Game logic
        map_mousex = math.floor(mousex / 32)
        map_mousey = math.floor(mousey / 32)

        if gameboard[map_mousex][map_mousey] == 0 and left == True:
            gameboard[map_mousex][map_mousey] = 1
        # elif gameboard[map_mousex][map_mousey] == 1 and right == True:
        #    gameboard[map_mousex][map_mousey] = 0

        play = capture_piece(gameboard, map_mousex, map_mousey, "player")
        if play[0] >= 0:
            gameboard[play[0]][play[1]] = 1

        move = 0,0
        # dumb computer move.  It's going to put out a square at a random spot on the map
        while comp_turn:
            move = comp_brain.calculate_move(gameboard)
            comp_turn = False

            gameboard[move[0]][move[1]] = 2
            
            play = capture_piece(gameboard, move[0], move[1], "computer")
            if play[0] >= 0:
                gameboard[play[0]][play[1]] = 2

        
        for j in range(HEIGHT):
            for k in range(WIDTH):
                if gameboard[k][j] == 0:
                    pygame.draw.rect(window, WHITE, [k * 32, j * 32, 32, 32], 0)
                elif gameboard[k][j] == 1:
                    pygame.draw.rect(window, RED, [k * 32, j * 32, 32, 32], 0)
                elif gameboard[k][j] == 2:
                    pygame.draw.rect(window, GREEN, [k * 32, j * 32, 32, 32], 0)

        for x in range(WIDTH):
            pygame.draw.line(window, BLACK, ((x * 32),0), ((x * 32),(HEIGHT * 32))) 
            for y in range(WIDTH):
                pygame.draw.line(window, BLACK, (0 , (y * 32)), ((WIDTH * 32),(y * 32)))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()