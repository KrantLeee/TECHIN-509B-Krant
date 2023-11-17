# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import random
from logic import business_logic

# User Interaction
class user_interaction:
    def __init__(self, logic):
        self.logic = logic
        
    def show_board(self):
        for i, row in enumerate(self.logic.board):
            display_row = [' ' if cell == None else cell for cell in row]
            print(' | '.join(display_row))
            if i < 2:
                print('——'*5)

    def get_user_move(self):
        while True:
            self.user_input = input('Please make your movement by typing x,y (e.g., 1,2):').split(',')
            user_input = self.user_input
            if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit(): # Check if the input is legal
                x, y = int(user_input[0]), int(user_input[1])
                if 0 <= x <= 2 and 0 <= y <= 2: # Check if the input is within boundary
                    if self.logic.board[x][y] is None:  # Check if the position is empty
                        return x, y
                    else:
                        print("This position is already taken. Please choose another one.")
                else:
                    print("Invalid coordinates. Please enter values between 0 and 2.")
            else:
                print("Invalid input. Please enter in the format x,y.")

    def get_computer_move(self):
        empty_cells = [(a, b) for a in range (3) for b in range(3) if self.logic.board[a][b] is None]
        return random.choice(empty_cells)
        
# Use case
class use_case:
    def play(self):
        #Choose a mode
        mode = input("Choose a mode (1 for single-player, 2 for double-player): ").strip()
        while mode not in ['1', '2']:
            print("Invalid input. Please choose 1 for single-player or 2 for two-player.")
            mode = input("Choose a mode (1 for single-player, 2 for two-player): ").strip()

        logic = business_logic()
        ui = user_interaction(logic)  #This ui has atrribute 'logic' as a instance of business_logic and all the methods from user_interaction
        #self.board = business_logic.make_empty_board()
        winner = None
        print("TODO: take a turn!")

        while winner == None:
            next_player = logic.next_player() #Use instance to call the function
            ui.show_board()
            # TODO: Update who's turn it is.
            print(f"It's {logic.next_player()}'s turn!")

            #Check the mode,  input a move from the computer or player
            if mode == '1' and next_player == 'O':
                x,y = ui.get_computer_move()
            else:
                x, y = ui.get_user_move()
            logic.board[x][y] = next_player

            #TODO: Check winner.
            winner = logic.get_winner(next_player)
            if winner:
                print (winner, 'wins!')
                break

            # Check for a draw
            if not winner:
                if logic.check_draw():
                    print("It's a draw!")
                    break
        ui.show_board()                

