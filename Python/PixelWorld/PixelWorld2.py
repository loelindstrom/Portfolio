import tkinter as tk
import random

class FrameArray(list):
    def __init__(self):
        '''
        A class to be used in the PixelWorld class.
        It's a list constructed as a 2D array containing
        tkinter's tk.Frame()-objects.
        The frames in the array can be accessed easy with row and column index.
        The background of a frame can also be turned from white to black and vice versa.
        '''
        super().__init__()

    def get(self, row, column):
        '''
        Returns a frame from the array based on the row and column index of the frame.
        :param row: int
        :param column: int
        :return: Frame()
        '''
        return self[row][column]

    def turnoff(self, row, column):
        '''
        Turns the bakground of a frame at a certain row and column in the array
        from black to white.
        :param row: int
        :param column: int
        :return: None
        '''
        frame = self[row][column]
        frame.configure(bg='white')

    def turnon(self, row, column):
        '''
        Turns the bakground of a frame at a certain row and column in the array
        from white to black.
        :param row:
        :param column:
        :return:
        '''
        frame = self[row][column]
        frame.configure(bg='black')

class PixelObject():
    def __init__(self, pixel_coordinates):
        '''
        A class for keeping track of objects in a PixelWorld().
        A PixelObject consists of several pixels which are kept track of
        by its pixel coordinates.
        The PixelObject can be moved around in the PixelWorld().
        :param pixel_coordinates: a list with coordinate pairs, each coordinate pair is in their own list.
        '''
        self.pixel_coordinates = pixel_coordinates

    def move(self, direction):
        '''
        Moves an PixelObject's by updating its coordinates
        :param direction: String with direction of movement
        :return:
        '''
        if direction == "up":
            for pixel in self.pixel_coordinates:
                pixel[0] -= 1

        if direction == "down":
            for pixel in self.pixel_coordinates:
                pixel[0] += 1

        if direction == "right":
            for pixel in self.pixel_coordinates:
                pixel[1] += 1

        if direction == "left":
            for pixel in self.pixel_coordinates:
                pixel[1] -= 1

        return self.pixel_coordinates


class PixelWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        win_width = 600
        win_height = 700
        self.geometry(str(win_width) + "x" + str(win_height))

        # The frame keeping track of scores
        self.score = 0
        self.score_frame = tk.Frame(self, width=win_width, height=win_height/7, bg='lightgreen')
        self.score_frame.grid(row=0, column=0, sticky="nsew")
        self.textVar = tk.StringVar("")
        self.score_label = tk.Label(self.score_frame, textvariable=self.textVar)
        self.textVar.set("Score")
        self.score_label.pack(anchor=tk.CENTER, padx=20, pady=20, ipadx=10, ipady=10)

        # The frame where the pixels are situated
        pixelWorld_height = win_height - win_height / 7
        self.rows = 20
        self.columns = 20
        self.frame = tk.Frame(self)
        self.frame.grid(row=1, column=0, sticky="nsew")

        p_height = (pixelWorld_height) / self.rows
        p_width = (win_width) / self.columns

        self.all_frames = FrameArray()
        for row in range(self.rows):
            row_for_array = []
            for col in range(self.columns):
                f = tk.Frame(self.frame, width=p_width, height=p_height, bd=1, relief='ridge')
                f.grid(row=row, column=col)
                row_for_array.append(f)
            self.all_frames.append(row_for_array)

    def renderPixelObjectList(self, POlist):
        for PO in POlist:
            self.renderPixelObject(PO)


    def renderPixelObject(self, PixelObject):
        for coordinates in PixelObject.pixel_coordinates:
            self.all_frames.turnon(coordinates[0], coordinates[1])

    def userMove(self, event, PixelObject, move_dict):
        dir = move_dict[event.keysym]
        for coordinates in PixelObject.pixel_coordinates:
            row, column = coordinates[0], coordinates[1]
            self.all_frames.turnoff(row, column)

        PixelObject.move(dir)

        for coordinates in PixelObject.pixel_coordinates:
            row, column = coordinates[0], coordinates[1]
            self.all_frames.turnon(row, column)


# PW = PixelWorld()
# PW.mainloop()