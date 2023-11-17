from logic import business_logic
from cli import user_interaction
from cli import use_case

#game start
if __name__ == '__main__':
    game = use_case()
    game.play()