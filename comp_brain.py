import random


class Bot:
    def __init__(self, level):
        self.level = level

    def calculate_move(self, gameboard):

        move = 0,0

        # From our x and y position, let's check the 8 cardinal points 
        north = True
        south = True
        east = True
        west = True
        north_east = True
        south_east = True
        south_west = True
        north_west = True

        valid_move = False
        while not valid_move:
            nextX = random.randrange(24)
            nextY = random.randrange(17)

            print (str(nextX) + " : " + str(nextY))

            # Let's see if we can put bounds on our bot brain
            if nextX + 2 > 24:
                east = False
                north_east = False
                south_east = False

            if nextX - 2 < 0:
                west = False
                north_west = False
                south_west = False

            if nextY - 2 < 0:
                north = False
                north_west = False
                north_east = False

            if nextY + 2 > 17:
                south = False
                south_west = False
                south_east = False

            move = random.randrange(8)
            # north = 0, east = 1, south = 2, west = 3, north_east = 4, south_east = 5, south_west = 6, north_west = 7
            
            if move == 0 and north:
                if gameboard[nextX][nextY - 2] == 0:
                    gameboard[nextX][nextY - 2] = 2
                    move = nextX, nextY - 2
                    valid_move = True
                    return move
            elif move == 1 and east:
                if gameboard[nextX + 2][nextY] == 0:
                    gameboard[nextX + 2][nextY] = 2
                    move = nextX + 2, nextY
                    valid_move = True
                    return move
            
            elif move == 2 and south:
                if gameboard[nextX][nextY + 2] == 0:
                    gameboard[nextX][nextY + 2] = 2
                    move = nextX, nextY + 2
                    valid_move = True
                    return move

            elif move == 3 and west:
                if gameboard[nextX - 2][nextY] == 0:
                    gameboard[nextX - 2][nextY] = 2
                    move = nextX - 2, nextY
                    valid_move = True
                    return move

            elif move == 4 and north_east:
                if gameboard[nextX + 2][nextY - 2] == 0:
                    gameboard[nextX][nextY - 2] = 2
                    move = nextX, nextY - 2
                    valid_move = True
                    return move
            elif move == 5 and south_east:
                if gameboard[nextX + 2][nextY - 2] == 0:
                    gameboard[nextX + 2][nextY - 2] = 2
                    move = nextX + 2, nextY - 2
                    valid_move = True
                    return move

            elif move == 6 and south_west:
                if gameboard[nextX - 2][nextY + 2] == 0:
                    gameboard[nextX - 2][nextY + 2] = 2
                    move = nextX - 2, nextY + 2
                    valid_move = True
                    return move

            elif move == 7 and north_west:
                if gameboard[nextX - 2][nextY - 2] == 0:
                    gameboard[nextX - 2][nextY - 2] = 2
                    move = nextX - 2, nextY - 2
                    valid_move = True
                    return move
            else:
                print("No valid move! Trying agian")
