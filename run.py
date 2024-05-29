#Project Imports
import random

#Lists and Dictionaries to be Used Throughout
ship_length = [2,3,4,5]

user_board = [[" "] * 8 for i in range(8)] #Decided on size of the player board, TODO add variable board size
comp_board = [[" "] * 8 for i in range(8)] #Decided on size of the computer board, TODO add variable board size

user_guess_board = [[" "] * 8 for i in range(8)]
comp_guess_board = [[" "] * 8 for i in range(8)]

nums_as_letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} #Dictionary to convert text inputs to numerical for move tracking

#Creating Generic Board Layout
def create_board(board):
    print("    A  B  C  D  E  F  G  H")
    print("============================")
    row_num = 1
    for row in board:
        print("%d |%s |" % (row_num, " |".join(row)))
        row_num += 1

#Start Placing Ships on the Board
def launch_ships(board):
    #Move through all ships
    for ships in ship_length:
        while True:
            if board == comp_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_space(ships, row, column, orientation):


#Ensure that Ships with on the Board
def check_space(ship_length, row, column, orientation):
    if orientation == "H":
        if column + ship_length > 8:
            return False
        else:
            return True
    else:
        if row + ship_length > 8:
            return False
        else:
            return True

#Ensure that Ships fo not Overlap
def ship_overlap(board, row, column, orientation, ships):
    if orientation == "H":
        for i in range(column, column + ships):
            if board[row][i] == "X":
                return True
    else:
        for i in range((row, row + ships)):
            if board[i][column] == "X":
                return True

create_board(user_board)