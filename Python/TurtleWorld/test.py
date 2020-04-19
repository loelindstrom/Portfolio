import tkinter as tk

wn = tk.Tk()
frame = tk.Frame(wn, bg='black', width=500, height=500)
frame.pack()

counter = 0

def changeBackground():
    global counter, wn
    if counter%2 == 0:
        frame.configure(bg='white')
    else:
        frame.configure(bg='black')
    counter += 1
    wn.after(500, changeBackground)

changeBackground()
wn.mainloop()