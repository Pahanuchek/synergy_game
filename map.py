CELL_TYPES = '🏾🌲🌊🏩🏬'

class Map:
    #def generate_rivers(self):

    #def generate_forests(self):

    def print_map(self):
        print('⬛' * (self.w + 2))
        for row in self.cells:
            print('⬛', end='')
            for cell in row:
                if (cell >= 0 or cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print('⬛', end='')
            print()
        print('⬛' * (self.w + 2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.w or x >= self.h):
            return False
        else:
            True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

tmp = Map(20, 10)
tmp.print_map()