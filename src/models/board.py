from token import Token
from player import Player

class Board:

    """
    Class Board is designed to store the main board of the game with dynamic size n x k
    """

    def __init__ (self, _w: int, _h: int, _win_cond: int) -> None:
        # Constructor variables
        self.w = _w     # Boards width
        self.h = _h     # Boards height
        self.win_cond = _win_cond   # Wining condition, how many tokens in line are needed

        # Created variables
        self.grid = [[None for _ in range(self.w)] for _ in range(self.h)]  #Create initial grid

    # Print board (in console)
    def print_board(self) -> None:
        for row in range(self.h):
            for col in range(self.w):
                print(self.grid[row][col], end=' ')
                print(' ', end=' ')

    # Render board
    #def render_board(self):

    # Determine coordinates of first empty row in chosen column
    def get_first_empty_cell(self, col: int):
        for row in range(self.h):
            if self.grid[row][col] is None:
                continue
            else:
                return row
        return None

    # Push token into one of the columns
    def move(self, col: int, color: int,):
        # TODO VALIDATE ROW AND COLOR
        row = self.get_first_empty_cell(col)

        if row is None:
            print("Column is already filled chose another one")
            return None
        else:
            token = Token(row, col, color)
            self.grid[row][col] = token
            return None

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

        # Set counter to check how many tokens in line are there
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
                    break

            # Clear combination in current row
            self.reset_dict_values(counter)


    # Check for empty cells / if there are no empty cell the game ends
    def check_empty_cells(self) -> bool:
        for row in range(self.h):
            for col in range(self.w):
                if self.grid[row][col] is None:
                    return True
        return False