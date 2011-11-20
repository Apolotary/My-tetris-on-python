class Defs:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Defs, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.cell_size =	18
        self.cols =		16
        self.rows =		20
        self.maxfps =   30

        self.colors = [
        (0,   0,   0  ),
        (255, 85,  85),
        (100, 200, 115),
        (120, 108, 245),
        (255, 140, 50 ),
        (50,  120, 52 ),
        (146, 202, 73 ),
        (150, 161, 218 ),
        (255,255,255),
        (255, 85,  85) # color for non-sticky board borders
        ]

    def check_collision(self, board, shape, offset):
        off_x, off_y = offset
        for cy, row in enumerate(shape): # we take one inner array
            for cx, cell in enumerate(row): # run within it and check colors
                try:
                    print(cy+off_y, cx+off_x, cell, board[ cy + off_y ][ cx + off_x ])
                    if cell and board[ cy + off_y][ cx + off_x ]: # if board and cell share the same color
                        return True                                # then we reached the end and game is over :)
                except IndexError:
                    return True
        return False

    def check_hcollision(self, board, shape, offset):
        # we can't stack figures horizontally
        off_x, off_y = offset
        counter = 0
        for cy, row in enumerate(shape): # we take one inner array
            for cx, cell in enumerate(row): # run within it and check colors
                    print(cy+off_y, cx+off_x, cell, board[ cy + off_y ][ cx + off_x ])
                    if not board[ cy + off_y + 1][ cx + off_x ]: # if board and cell share the same color
                        counter += 1                               # then we reached the end and game is over :)
        if counter >= (len (shape[0])):
            return False
        return True
