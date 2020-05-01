import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame = tk.Frame(self, bg='black', width=30, height=30)
        self.frame2 = tk.Frame(self, bg='white', width=30, height=30)
        self.frame.pack()
        self.frame2.pack()

        self.frames = [self.frame, self.frame2]
        self.bind('<a>', self.addLabel)

    def changeBackgrounds(self):
        for i, frame in enumerate(self.frames):
            if i % 2 == 0:
                frame.configure(bg='white')
            else:
                frame.configure(bg='black')
        self.frames = self.frames[::-1]
        print(self.frames)
        self.after(500, self.changeBackgrounds)

    def addLabel(self, event):
        print('hejhej')
        frame = tk.Frame(self, bg='black', width=30, height=30)
        frame.pack()



wn = MyApp()
wn.changeBackgrounds()
wn.mainloop()