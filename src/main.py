from src.models.board import Board
from src.models.player import Player
#from src.models.game_token import Token

def main():

    move_counter = 0

    # Initialize variable
    board = Board(7,6, 4) # TODO add yaml.config
    player_red = Player(0)
    player_blue = Player(1)

    # Main game loop
    while True:

        # First player move
        board.random_move(player_red)
        board.print_board()
        #check_win()

        # Second player move
        board.random_move(player_blue)
        board.print_board()
        #check_win()

        move_counter += 1
        if move_counter == 14:
            break



if __name__ == "__main__":
    main()
