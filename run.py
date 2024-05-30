#Importing Project Dependencies
import random

#Declaring Project Lists & Dictionaries 
ship_length_list = [2,3,3,4,5]  

user_board = [[" "] * 8 for i in range(8)]
comp_board = [[" "] * 8 for i in range(8)]

user_guess_board = [[" "] * 8 for i in range(8)]
comp_guess_board = [[" "] * 8 for i in range(8)]

letters_to_nums = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

#Build Basic Board Structure
def create_board(board):
    print("   A  B  C  D  E  F  G  H")
    print(" =========================")
    row_number = 1
    for row in board:
        print("%d |%s |" % (row_number, " |".join(row)))
        row_number += 1

#Place Ships on the Boards
def launch_ships(board):
    #Loop Through Length of Ships
    for ship_length in ship_length_list:
        #Loop Until Ship Fits and Doesn't Overlap
        while True:
            if board == comp_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
                if check_space(ship_length, row, column, orientation):
                    #Check if Ship Overlaps
                    if ship_collisions(board, row, column, orientation, ship_length) == False:
                        #Place Ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_space(ship_length, row, column, orientation):
                    #Check if Ship Overlaps
                        if ship_collisions(board, row, column, orientation, ship_length) == False:
                            #Place Ship
                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                            create_board(user_board)
                            break 

#Check that the Ship fits on the Board
def check_space(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True

#Ensure that the Ships do not Overlap Each Other
def ship_collisions(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False

#Handling User Inputs
def user_input(place_ship):
    #Placing User Ships on the Board
    if place_ship == True:
        while True:
            try: 
                orientation = input("Please select an Orientation (H or V): \n").upper() #Converting to Uppercase to Prevent Input Errors
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Please select a valid Orientation H or V \n')
        while True:
            try: 
                row = input("Please select a row to place your ship (1 - 8): \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Please select a valid row (1 - 8) \n')
        while True:
            try: 
                column = input("Please select a column to place your ship (A - H): \n").upper() #Converting to Uppercase to Prevent Input Errors
                if column in 'ABCDEFGH':
                    column = letters_to_nums[column]
                    break
            except KeyError:
                print('Please select a valid Column (A - H) \n')
        return row, column, orientation 
    else:
        #Guessing Computer Ship Locations
        while True:
            try: 
                row = input("Select a row to target an Enemy Ship (1 - 8): \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Please select a valid row (1 - 8) \n')
        while True:
            try: 
                column = input("Select a column to target an Enemy Ship (A - H): \n").upper() #Converting to Uppercase to Prevent Input Errors
                if column in 'ABCDEFGH':
                    column = letters_to_nums[column]
                    break
            except KeyError:
                print('Please select a valid Column (A - H) \n')
        return row, column        

#Check When All SHips Hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

#Turn Manager - User & Computer
def turn(board):
    if board == user_guess_board:
        row, column = user_input(user_guess_board)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif comp_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif user_board[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

#Print Boards Each Turn
launch_ships(comp_board)
#create_board(comp_board)

create_board(user_board)
launch_ships(user_board)
        
while True:
    #Player Turn Handling
    while True:
        print('Guess a battleship location \n')
        create_board(user_guess_board)
        turn(user_guess_board)
        break
    if count_hit_ships(user_guess_board) == 17:
        print("You win!")
        break   
    #computer turn
    while True:
        turn(comp_guess_board)
        break           
    create_board(comp_guess_board)   
    if count_hit_ships(comp_guess_board) == 17:
        print("Sorry, the computer won.")
        break