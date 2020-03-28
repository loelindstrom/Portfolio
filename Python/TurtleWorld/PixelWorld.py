import tkinter as tk

class PixelWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        win_width = 800
        win_height = 800
        self.geometry(str(win_width) + "x" + str(win_height))

        rows = 40
        columns = 40


        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky="nsew")


        p_height = (win_height) / rows
        p_width = (win_width) / columns

        all_frames = []
        for row in range(rows):
            row_for_array = []
            for col in range(columns):
                f = tk.Frame(frame, width=p_width, height=p_height, bd=1, relief='ridge')
                if col % 2 == 0 and row % 2 == 0:
                    f.configure(bg='black')
                f.grid(row=row, column=col)
                row_for_array.append(f)
            all_frames.append(row_for_array)

PW = PixelWorld()
PW.mainloop()