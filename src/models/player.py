import random

from .board import Board
from .game_token import GameToken

class Player:

    def __init__(self, _color: int) -> None:
        self.color = _color

    # Push token into one of the columns
    def move(self, board: Board, col: int, ) -> None:

        # TODO VALIDATE ROW AND COLOR
        row = board.get_first_empty_cell(col)

        if row is None:
            print("Column is already filled chose another one")

            return None
        else:
            # Create token and insert it into the grid
            token = GameToken(self.color, row, col, )
            board.grid[row][col] = token

            return None

    # Push token into random column
    def random_move(self, board: Board) -> None:
        # Get all viable moves
        viable_moves = board.get_all_viable_cols()

        # Chose random col and insert token
        random_move_col = random.choice(viable_moves)
        self.move(board, random_move_col)