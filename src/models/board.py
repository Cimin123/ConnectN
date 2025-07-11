import random

from .game_token import GameToken
from .player import Player

class Board:

    """
    Class Board is designed to store the main board of the game with dynamic size w x h
    """

    def __init__ (self, _w: int, _h: int, _win_cond: int) -> None:

        # Constructor variables
        self.w = _w     # Boards width
        self.h = _h     # Boards height
        self.win_cond = _win_cond   # Wining condition, how many tokens in line are needed to win

        # Created variables
        self.grid = self.create_initial_grid() #Create initial grid

    # Initialize the board
    def create_initial_grid(self):
        grid = [[None for _ in range(self.w)] for _ in range(self.h)]
        return grid

    # Print board (in console)
    def print_board(self) -> None:
        for row in range(self.h):
            for col in range(self.w):
                cur_cell = self.grid[row][col]

                if cur_cell is None:
                    print(self.grid[row][col], end=' ')
                else:
                    print(self.grid[row][col].color, end=' ')

            print()
        print()

    # Render board
    #def render_board(self):

    # Determine coordinates of first empty row in chosen column
    def get_first_empty_cell(self, col: int):
        for row in range(self.h):
            if self.grid[row][col] is None:
                return row
            else:
                continue
        return None

    # Get all viable cols for the move
    def get_all_viable_cols(self) -> list:

        # List of viable columns
        viable_cols = []

        for col in range(self.w):
            if self.get_first_empty_cell(col) is not None:
                viable_cols.append(col)

        return viable_cols

    #def check_move(self):
    # Reset dict etc. if whole row was scanned without finding winning combination, then reset the counter
    def reset_dict_values(d: dict) -> None:
        for key in d:
            d[key] = 0

    # Check if dict consists of winning combination
    def check_streak(self, d: dict) -> bool:
        for key in d:
            if d[key] == self.win_cond:
                return True
        return False

    # Check win horizontal orientation
    def check_horizontal_win(self) -> bool:

        # Set counter to check how many tokens in line are there for both players
        counter = {
            0: 0,
            1: 0
        }

        for row in range(self.h):
            for col in range(self.w):
                current_token = self.grid[row][col]

                if current_token is None:   # If empty cell encountered continue
                    continue
                else:
                    counter[current_token.color] += 1

                if self.check_streak(counter):
                    print(f"Game Over player {current_token.color} won!")
                    return True

            # Clear combination in current row
            self.reset_dict_values(counter)

        return False


    # Check for empty cells / if there are no empty cell the game ends
    def check_empty_cells(self) -> bool:
        for row in range(self.h):
            for col in range(self.w):
                if self.grid[row][col] is None:
                    return True
        return False