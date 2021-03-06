class Pixel():
    def __init__(self, row, column, np_array):
        self.row = row
        self.column = column
        self.world = np_array

    def index(self):
        return self.row, self.column

    def willStayInWorld(self, param):
        world_rows, world_columns = self.world.shape

        if isinstance(param, tuple):
            row, column = param

        else:
            if param not in [1, 2, 3, 4]:
                return False
            if param == 1 or param == 2:
                row = self.row + self.translatedDirection(param)
                column = self.column

            if param == 3 or param == 4:
                row = self.row
                column = self.column + self.translatedDirection(param)

        if not 0 <= row < world_rows:
            return False

        if not 0 <= column < world_columns:
            return False

        return True

    def turnOff(self):
        self.world[self.index()] = 0

    def turnOn(self):
        self.world[self.index()] = 1

    def update_coordinates(self, direction):
        if self.willStayInWorld(direction):

            if direction == 1 or direction == 2:
                self.row += self.translatedDirection(direction)

            if direction == 3 or direction == 4:
                self.column += self.translatedDirection(direction)

    def move(self, direction):
        self.turnOff()
        self.update_coordinates(direction)
        self.turnOn()

    def teleportTo(self, row, column):
        if self.willStayInWorld((row, column)):
            self.turnOff()
            self.row = row
            self.column = column
            self.turnOn()

    @staticmethod
    def translatedDirection(direction):
        if direction == 1 or direction == 3:
            return -1
        if direction == 2 or direction == 4:
            return 1