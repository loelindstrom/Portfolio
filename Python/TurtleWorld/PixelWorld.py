import tkinter as tk

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

        all_frames = []
        for row in range(rows):
            row_for_array = []
            for col in range(columns):
                f = tk.Frame(self.frame, width=p_width, height=p_height, bd=1, relief='ridge')
                # if col % 2 == 0 and row % 2 == 0:
                #     f.configure(bg='black')
                f.grid(row=row, column=col)
                row_for_array.append(f)
            all_frames.append(row_for_array)

        self.dot = self.frame.grid_slaves(self.row_count, self.col_count)[0]
        self.dot.configure(bg='black')

        self.bind('<Right>', self.wandering)

    def wandering(self, event):
        self.row_count += 1
        self.col_count += 1
        print(self.row_count, self.col_count)
        self.dot.configure(bg='white')
        self.dot = self.frame.grid_slaves(self.row_count, self.col_count)[0]
        self.dot.configure(bg='black')


PW = PixelWorld()
# PW.wandering()
PW.mainloop()