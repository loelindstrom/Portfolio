import tkinter as tk

class FrameArray(list):
    def __init__(self):
        super().__init__()

    def get(self, row, column):
        return self[row][column]

    def turnoff(self, row, column):
        frame = self[row][column]
        frame.configure(bg='white')

    def turnon(self, row, column):
        frame = self[row][column]
        frame.configure(bg='black')

class PixelObject():
    def __init__(self, pixel_coordinates):
        self.pixel_coordinates = pixel_coordinates

    def move(self, direction):
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
        self.score_frame = tk.Frame(self, width=win_width, height=win_height/7, bg='lightgreen')
        self.score_frame.grid(row=0, column=0, sticky="nsew")
        self.textVar = tk.StringVar("")
        self.score_label = tk.Label(self.score_frame, textvariable=self.textVar)
        self.textVar.set("Score")
        self.score_label.pack(anchor=tk.CENTER, padx=20, pady=20, ipadx=10, ipady=10)

        # The frame where the pixels are situated
        pixelWorld_height = win_height - win_height / 7
        rows = 20
        columns = 20
        self.frame = tk.Frame(self)
        self.frame.grid(row=1, column=0, sticky="nsew")

        p_height = (pixelWorld_height) / rows
        p_width = (win_width) / columns

        self.all_frames = FrameArray()
        for row in range(rows):
            row_for_array = []
            for col in range(columns):
                f = tk.Frame(self.frame, width=p_width, height=p_height, bd=1, relief='ridge')
                f.grid(row=row, column=col)
                row_for_array.append(f)
            self.all_frames.append(row_for_array)

        # Objects in the PixelWorld:
        # self.dot = PixelObject([[0,0]])
        # self.line = PixelObject([[0,10], [1,10], [2,10], [3,10]])
        # self.cross = PixelObject([[0,5], [1,4], [1,6], [2,5]])
        # my_list = [self.dot, self.line, self.cross]
        # self.renderPixelObjectList(my_list)


        self.user_basket = PixelObject([[18,8], [19,8], [19,9], [19,10], [19,11], [18,11]])
        self.renderPixelObject(self.user_basket)


        # For making the user able to move the agent:
        self.move_dict = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}
        for cmd in zip(['<w>', '<a>', '<s>', '<d>']):
                self.bind(cmd, self.userMove)


    def renderPixelObjectList(self, POlist):
        for PO in POlist:
            self.renderPixelObject(PO)


    def renderPixelObject(self, PixelObject):
        for coordinates in PixelObject.pixel_coordinates:
            frame = self.all_frames[coordinates[0]][coordinates[1]]
            frame.configure(bg='black')

    def move_dot(self):
        dir = 'down'
        for coordinates in self.dot.pixel_coordinates:
            row, column = coordinates[0], coordinates[1]
            self.all_frames.turnoff(row, column)

        self.dot.move(dir)

        for coordinates in self.dot.pixel_coordinates:
            row, column = coordinates[0], coordinates[1]
            self.all_frames.turnon(row, column)

        self.after(2000, self.move_dot)

    def userMove(self, event):
        dir = self.move_dict[event.keysym]
        for coordinates in self.user_basket.pixel_coordinates:
            row, column = coordinates[0], coordinates[1]
            self.all_frames.turnoff(row, column)

        self.user_basket.move(dir)

        for coordinates in self.user_basket.pixel_coordinates:
            row, column = coordinates[0], coordinates[1]
            self.all_frames.turnon(row, column)

PW = PixelWorld()
# PW.move_dot()
PW.mainloop()