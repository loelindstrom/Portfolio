import numpy as np

class Pixel():
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def index(self):
        return self.row, self.column


class PixelWorld():
    def __init__(self):
        self.world = np.zeros((20,20))
        self.p = Pixel(1, 1)
        self.world[self.p.index()] = 1
        while True:
            dir = int(input("Press 0,1,2,3: "))
            self.move_pixel(self.p, dir)
            print(self.world)



    def move_pixel(self, pixel, dir):
        self.world[pixel.index()] = 0

        if dir == 0:
            pixel.row -= 1
        if dir == 1:
            pixel.row += 1
        if dir == 2:
            pixel.column -= 1
        if dir == 3:
            pixel.column += 1

        self.world[pixel.index()] = 1



PW = PixelWorld()
