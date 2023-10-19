from typing import List

'''board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]'''

board = [
    "......................",
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]



def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    for row in range(len(input_board)):
      input_board[row] = list(input_board[row])
      #print(input_board)

    if input_board[x][y] == new:
        return input_board
    def filler(x,y):
      if 0 <= x < len(input_board) and 0 <= y < len(input_board[0]) and input_board[x][y] == old:
        input_board[x][y] = new
        filler(x+1,y)
        filler(x-1,y)
        filler(x,y+1)
        filler(x,y-1)
    filler(x,y)
    input_board = [''.join(row2) for row2 in input_board]
    return input_board



    

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

