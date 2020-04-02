import tkinter as tk

class FrameArray(list):
    def __init__(self):
        super().__init__()

    def get(self, row, column):
        return self[row][column]

class Cross():
    def __init__(self, top, left, right, bottom):
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom

    def move(self, direction):
        if direction == "up":
            self.top -= 1
            self.bottom -= 1

        if direction == "down":
            self.top += 1
            self.bottom += 1

        if direction == "right":
            self.left += 1
            self.right += 1

        if direction == "left":
            self.left -= 1
            self.right -= 1

class PixelWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        win_width = 800
        win_height = 800
        self.geometry(str(win_width) + "x" + str(win_height))

        rows = 40
        columns = 40

        self.row_count = 0
        self.col_count = 0

        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, sticky="nsew")


        p_height = (win_height) / rows
        p_width = (win_width) / columns

        self.all_frames = []
        for row in range(rows):
            row_for_array = []
            for col in range(columns):
                f = tk.Frame(self.frame, width=p_width, height=p_height, bd=1, relief='ridge')
                # if col % 2 == 0 and row % 2 == 0:
                #     f.configure(bg='black')
                f.grid(row=row, column=col)
                row_for_array.append(f)
            self.all_frames.append(row_for_array)

        self.dot = self.frame.grid_slaves(self.row_count, self.col_count)[0]
        self.dot.configure(bg='black')


        self.tR = 0
        self.tC = 5
        self.lR = 1
        self.lC = 4
        self.rR = 1
        self.rC = 6
        self.dR = 2
        self.dC = 5

        self.cross = [self.all_frames[self.tR][self.tC], self.all_frames[self.lR][self.lC], self.all_frames[self.rR][self.rC], self.all_frames[self.dR][self.dC]]
        for frame in self.cross:
            frame.configure(bg='black')

        self.bind('<Right>', self.wandering)
        self.bind('<Down>', self.falling_cross)

    def wandering(self, event):
        self.row_count += 1
        self.col_count += 1
        print(self.row_count, self.col_count)
        self.dot.configure(bg='white')
        self.dot = self.frame.grid_slaves(self.row_count, self.col_count)[0]
        self.dot.configure(bg='black')

    def falling_cross(self, event):
        for frame in self.cross:
            frame.configure(bg='white')
        self.tR += 1
        self.lR += 1
        self.rR += 1
        self.dR += 1
        self.cross = [self.all_frames[self.tR][self.tC], self.all_frames[self.lR][self.lC],
                      self.all_frames[self.rR][self.rC], self.all_frames[self.dR][self.dC]]
        for frame in self.cross:
            frame.configure(bg='black')


PW = PixelWorld()
# PW.wandering()
PW.mainloop()