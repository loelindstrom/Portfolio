# Written for Python 3.7
# By Loe Lindström

import turtle

class TurtleWorld():
    def __init__(self, rows=50, columns=50):
        # Screen initiations
        self.screen = turtle.Screen()
        # self.rootwindow = self.screen.getcanvas().winfo_toplevel()
        # self.rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        # self.rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

        # Calculating the size of the visual array in accordance to the size of the window.
        tkinter_canvas = self.screen.getcanvas()
        win_height = tkinter_canvas.winfo_height()
        win_width = tkinter_canvas.winfo_width()
        p_height = (win_height - 100) / rows
        p_width = (win_width - 100) / columns
        start_pos = [-(p_width * columns / 2), p_height * rows / 2]


        turtle.tracer(0, 0)

        self.array_w_turtles = Turtle2dArray()

        # Paint the turtles:
        for row in range(rows):
            row_for_array = []
            for col in range(columns):
                pix_turt = PixelTurtle(self.screen, width=p_width, height=p_height, start_pos=start_pos)
                pix_turt.paint_pixel()
                start_pos[0] += p_width
                row_for_array.append(pix_turt)
            start_pos[0] = -(p_width * columns / 2)
            start_pos[1] -= p_height
            self.array_w_turtles.append(row_for_array)
            turtle.update()


class PixelTurtle(turtle.RawTurtle):
    def __init__(self, parent, width, height, start_pos):
        super().__init__(parent)
        self.p_width = width
        self.p_height = height
        self.start_pos = start_pos

        # Hide and place the turtle in the right position:
        self.ht()
        self.pu()
        self.goto(self.start_pos)

    def paint_pixel(self, fill=False):
        self.pd()
        if fill:
            self.begin_fill()
        for _ in range(2):
            self.fd(self.p_width)
            self.right(90)
            self.fd(self.p_height)
            self.right(90)
        if fill:
            self.end_fill()



class Turtle2dArray(list):
    '''
    A 2-dimensional array in python's in-built list-format.
    But with the capability of getting the right index using tuples instead of the list-indexing
    python uses.
    '''

    def get_turtle(self, row, column):
        return self[row][column]


TW = TurtleWorld()
PT = TW.array_w_turtles.get_turtle(1, 1)
PT.paint_pixel(fill=True)
turtle.mainloop()
