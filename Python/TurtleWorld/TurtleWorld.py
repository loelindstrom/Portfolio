import turtle
import random
import time
screen = turtle.Screen()

turtlepower = []

turtle.tracer(0, 0)

cols = 10
rows = 10

startpos = [-300, 300]

class Turtle2dArray(list):
    '''
    A 2-dimensional array in python's in-built list-format.
    But with the capability of getting the right index using tuples instead of the list-indexing
    python uses.
    '''
    def __init__(self):
        super().__init__()

    def get_turtle(self, row, column):
        return self[row][column]


array_w_turtles = []
array_w_turtles = Turtle2dArray()

for row in range(rows):
    row_for_array = []
    for col in range(cols):
        t = turtle.Turtle()
        t.ht()
        t.pu()
        t.goto(startpos)
        t.pd()
        # t.
        for i in range(4):
            t.fd(60)
            t.right(90)
        startpos[0] += 60
        row_for_array.append(t)
    startpos[0] = -300
    startpos[1] -= 60
    array_w_turtles.append(row_for_array)


# for i in range(10):
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.goto(random.random()*500, random.random()*1000)
#     turtlepower.append(t)
#
# for i in range(1000):
#     turtle.stamp()

turtle.update()

screen.mainloop()

# time.sleep(3)