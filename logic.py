# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

#Business Logic
class business_logic:
    def __init__(self, message = "Take a turn!"):
        self.board = self.make_empty_board()
        self.winner = None
        print(message)

    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


    def get_winner(self, player):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        
        # Check rows, columns, and diagonals
        board = self.board
        winning = any(
            (board[i][0] == board[i][1] == board[i][2] == player) or  # rows
            (board[0][i] == board[1][i] == board[2][i] == player) or  # columns
            (board[0][0] == board[1][1] == board[2][2] == player) or  # top-left to bottom-right diagonal
            (board[0][2] == board[1][1] == board[2][0] == player)    # top-right to bottom-left diagonal
            for i in range(3)
        )
        return player if winning else None

    def check_draw(self):
        return all(cell is not None for row in self.board for cell in row)

    def next_player(self):
        """Count the current X and O numbers to find the next player."""
        num_X = sum(row.count('X') for row in self.board)
        num_O = sum(row.count('O') for row in self.board)
        return 'X' if num_X == num_O else 'O'
    
   

