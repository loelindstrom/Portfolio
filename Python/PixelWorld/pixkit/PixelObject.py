from .Pixel import Pixel

class PixelObject(list):
    def __init__(self, coordinates, np_array):

        for row, column in coordinates:
            pixel = Pixel(row, column, np_array)
            self.append(pixel)

    def turnOn(self):
        for pixel in self:
            pixel.turnOn()

    def turnOff(self):
        for pixel in self:
            pixel.turnOff()

    def willStayInWorld(self, direction):
        for pixel in self:
            if not pixel.willStayInWorld(direction):
                return False
        return True

    def move(self, direction):
        if self.willStayInWorld(direction):
            self.turnOff()
            for pixel in self:
                pixel.update_coordinates(direction)
            self.turnOn()