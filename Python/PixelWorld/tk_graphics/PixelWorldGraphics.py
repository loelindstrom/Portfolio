import tkinter as tk
from tk_graphics.FrameArray import FrameArray

class PixelWorldGraphics(tk.Tk):
    def __init__(self, rows, columns, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        win_width = 700
        win_height = 700
        self.geometry(str(win_width) + "x" + str(win_height))

        self.rows = rows
        self.columns = columns
        self.frame = tk.Frame(self)
        self.frame.grid(row=1, column=0, sticky="nsew")

        p_height = win_height / self.rows
        p_width = win_width / self.columns

        self.all_frames = FrameArray()
        for row in range(self.rows):
            row_for_array = []
            for col in range(self.columns):
                f = tk.Frame(self.frame, width=p_width, height=p_height, bd=1, relief='ridge')
                f.grid(row=row, column=col)
                row_for_array.append(f)
            self.all_frames.append(row_for_array)