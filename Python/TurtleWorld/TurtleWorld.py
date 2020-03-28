# Written for Python 3.7

import turtle
import random
import time
screen = turtle.Screen()
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

x = screen.getcanvas()
print(x.winfo_width())
print(x.winfo_height())

height = x.winfo_height()
width = x.winfo_width()

turtlepower = []

turtle.tracer(0, 0)

cols = 15
rows = 15

p_height = height / rows
p_width = width / cols

p_height = (height - (height/500)) / rows
p_width = (width - (width/500)) / cols

p_height = (height - 30) / rows
p_width = (width - 30) / cols

# startpos = [-300, 300]
startpos = [-(p_width*cols/2), p_height*rows/2]

class TurtleWorld():
    def __init__(self, rows=10, columns=10):
        # Screen initiations
        self.screen = turtle.Screen()
        self.rootwindow = self.screen.getcanvas().winfo_toplevel()
        self.rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        self.rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        turtle.tracer(0, 0)



        # Paint the turtles:
        for row in range(rows):
            row_for_array = []
            for col in range(columns):
                pt = PixelTurtle(self.screen)
                startpos[0] += 60
                row_for_array.append(pt)
            startpos[0] = -300
            startpos[1] -= 60
            array_w_turtles.append(row_for_array)


class PixelTurtle(turtle.RawTurtle):
    def __init__(self, parent, pixel_size, start_pos):
        super().__init__(parent)
        self.pixel_size = pixel_size
        self.start_pos = start_pos

        # Hide and place the turtle in the right position:
        self.ht()
        self.pu()
        self.goto(self.start_pos)

    def paint_pixel(self, fill=False):

        self.pd()
        # t.begin_fill()
        for i in range(4):
            self.fd(60)
            self.right(90)
        # t.end_fill()


class Turtle2dArray(list):
    '''
    A 2-dimensional array in python's in-built list-format.
    But with the capability of getting the right index using tuples instead of the list-indexing
    python uses.
    '''

    def get_turtle(self, row, column):
        return self[row][column]


array_w_turtles = Turtle2dArray()

for row in range(rows):
    row_for_array = []
    for col in range(cols):
        t = turtle.Turtle()
        t.ht()
        t.pu()
        t.goto(startpos)
        t.pd()
        # t.begin_fill()
        for i in range(2):
            for i in range(2):
                t.fd(p_width)
                t.right(90)
                t.fd(p_height)
                t.right(90)
        # t.end_fill()
        startpos[0] += p_width
        row_for_array.append(t)
    startpos[0] = -(p_width*cols/2)
    startpos[1] -= p_height
    array_w_turtles.append(row_for_array)


turtle.update()

turtle.mainloop()

# time.sleep(3)