#Project Imports
import random

#Creating Generic Board Layout
def create_board(board):
    print(" A  B  C  D  E  F  G  H")
    print("________________________")
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1