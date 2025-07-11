class GameToken:

    def __init__(self,
                 _x: int,
                 _y: int,
                 _color: int,
                 _sprite: str = 'sprite/path',
                 _h: int = 32,
                 _w: int = 32) -> None :

        self.x = _x     # Token coord in boards grid x-axis
        self.y = _y     # Token coord in board grid y-axis
        self.h = _h     # Token height in pixels
        self.w = _w     # Token width in pixels
        self.sprite = _sprite   # Token's sprite
        self.color = _color

    # Move token
    # def move(self, col_x: int) -> int:
