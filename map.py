from utils import randbool, randcell, randcell2

CELL_TYPES = '⬛🌲🌊🏩🏬'

class Map:
    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        if (self.check_bounds(rx, ry)):
            self.cells[rx][ry] = 2
            while l > 0:
                rc2 = randcell2(rx, ry)
                rx2, ry2 = rc2[0], rc2[1]
                if (self.check_bounds(rx2, ry2)):
                    self.cells[rx2][ry2] = 2
                    rx, ry = rx2, ry2
                    l -= 1


    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

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
        if (x < 0 or y < 0 or y >= self.w or x >= self.h):
            return False
        else:
            return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

tmp = Map(40, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(20)
tmp.generate_river(10)
tmp.generate_river(15)
tmp.print_map()