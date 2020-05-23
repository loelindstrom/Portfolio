import numpy as np
import tkinter as tk
import time
import pixkit as pxk
from tk_graphics.PixelWorldGraphics import PixelWorldGraphics

class DodgeTheRain():
    def __init__(self):
        self.rows = 20
        self.columns = 20
        self.world = np.zeros((self.rows, self.columns))

        self.counter = 0

        self.score = 0

        self.rain = []

        self.user = pxk.Pixel(19, 10, self.world)
        self.user.turnOn()

        while True:
            self.game_play(graphics=True)

    def game_play(self, graphics=False):
        self.make_rain()
        print(self.world)

        if graphics == True:
            self.graphic_win = PixelWorldGraphics(self.rows, self.columns)
            self.previous_turned_on = []


        while True:
            try:
                user_direction = int(input(""))
            except ValueError:
                user_direction = 0
            self.user.move(user_direction)
            self.move_rain()
            if self.counter % 2 == 0:
                self.make_rain()
            print(self.world)
            print(self.score)
            if graphics == True:
                self.render_graphics()
                self.graphic_win.update()
            self.counter += 1
            # time.sleep(0.5)



    def make_rain(self):
        if self.counter % 4 == 0:
            possible = list(range(0, self.rows, 2))
        else:
            possible = list(range(1, self.rows, 2))

        for i in range(2):
            rndm = np.random.randint(0, len(possible))
            column = possible.pop(rndm)
            drop = pxk.Pixel(0, column, self.world)
            drop.turnOn()
            self.rain.append(drop)

    def move_rain(self):
        to_remove = []
        for i, drop in enumerate(self.rain):
            if (drop.row, drop.column) == (self.user.row, self.user.column):
                self.score -= 50
                to_remove.append(i)
            elif not drop.willStayInWorld(2):
                to_remove.append(i)
            else:
                drop.move(2)

        for i in to_remove[::-1]:
            drop = self.rain.pop(i)
            drop.turnOff()
            del drop


    def render_graphics(self):
        rows, columns = np.where(self.world == 1)
        new_coordinates = zip(rows, columns)

        for coordinates in self.previous_turned_on:
            if coordinates not in zip(rows, columns):
                self.graphic_win.all_frames.turnOff(coordinates[0], coordinates[1])
            else:
                print("This was inside:", coordinates)

        self.previous_turned_on = []

        for row, column in new_coordinates:
            self.graphic_win.all_frames.turnOn(row, column)
            self.previous_turned_on.append((row, column))

FG = DodgeTheRain()