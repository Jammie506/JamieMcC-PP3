#Project Imports
import random

#Lists and Dictionaries to be Used Throughout
ship_length = [2,3,4,5]
user_board = [[" "] * 8 for i in range(8)]
comp_board = [[" "] * 8 for i in range(8)]

#Creating Generic Board Layout
def create_board(board):
    print("    A  B  C  D  E  F  G  H")
    print("============================")
    row_num = 1
    for row in board:
        print("%d |%s |" % (row_num, " |".join(row)))
        row_num += 1

create_board(user_board)