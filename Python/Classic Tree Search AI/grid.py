import turtle
import math
import copy


def turtlespecs(turtle, clr='black', speed=0, pu=True, ht=True):
    """
    A function to set parameters for a Turtle.Turtle()-instance.
    :param turtle: turtle.Turtle()
    :param clr: string with color.
    :param speed: int 0-10
    :param pu: Pen up
    :param ht: Hide-turtle
    """
    turtle.speed(speed)
    turtle.color(clr)
    if pu:
        turtle.pu()
    else:
        turtle.pd()
    if ht:
        turtle.ht()
    else:
        turtle.st()


class SimpleGrid:
    """
    A class to simulate actions in the Grid-class.
    Made to be able to play the game "Dots and Boxes".
    Created to work with a minimax-function.
    """
    def __init__(self, mademoves, boxes, connections, turn, greenscore, redscore):
        self.mademoves = mademoves
        self.boxes = boxes
        self.connections = connections
        self.turn = turn
        self.greenscore = greenscore
        self.redscore = redscore

    def get_moves(self):
        """
        Returns a list of moves that are available at the given SimpleGrid-instance.
        """
        lis = []
        for key in self.connections:
            if key not in self.mademoves:
                lis.append(key)
        return lis

    def try_move(self, key):
        """
        Creates a new SimpleGrid-instance and makes a move in that grid.
        :param key: an int which is a key in the dict()-instance self.connections
        :return: a SimpleGrid()-instance.
        """
        mademoves = copy.deepcopy(self.mademoves)
        boxes = copy.deepcopy(self.boxes)
        turn = copy.deepcopy(self.turn)
        greenscore = copy.deepcopy(self.greenscore)
        redscore = copy.deepcopy(self.redscore)
        next_state = SimpleGrid(mademoves, boxes, self.connections, turn, greenscore, redscore)
        next_state.mademoves.append(key)

        leave = False
        while next_state.is_there_box():
            if self.turn == 'green':
                next_state.greenscore += 1
            else:
                next_state.redscore += 1
            leave = True
        if leave:
            return next_state
        if self.turn == 'green':
            next_state.turn = 'red'
        else:
            next_state.turn = 'green'
        return next_state

    def is_there_box(self):
        """
        Checks if there is a box drawn in the grid and returns a bool.
        """
        for key in self.boxes:
            count = 0
            for line in self.boxes[key]:
                if line in self.mademoves:
                    count += 1
            if count == 4:
                del self.boxes[key]
                return True
        return False

    def isGameOver(self):
        """
        If there are no moves left in the grid, game is over.
        """
        if self.get_moves():
            return False
        return True

    def whoWon(self):
        """
        Counts the score and returns who won.
        """
        if self.greenscore > self.redscore:
            return 'green'
        if self.greenscore == self.redscore:
            return 'nobody'
        return 'red'

    def evaluate(self, player):
        """
        Evaluates the score for one player
        after the outcome of the game
        """
        if not self.isGameOver():
            return None
        if self.whoWon() == player:
            return 1
        if self.whoWon() == 'nobody':
            return 0
        return -1


class Grid:
    """
    A class to render the gameboard and keep track of parameters in the game "Dots and Boxes".
    Uses the turtle module
    """
    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.dots = []
        self.connections = dict()
        self.t = turtle.Turtle()
        self.gscore_turtle = turtle.Turtle()
        self.gscore_turtle.ht()
        self.rscore_turtle = turtle.Turtle()
        self.rscore_turtle.ht()
        self.turn = 'green'
        self.mademoves = []
        self.boxes = dict()
        self.greenscore = 0
        self.redscore = 0
        self.del_boxes = []

        self.verboseturtle = turtle.Turtle()
        turtlespecs(self.verboseturtle)
        self.verboseturtle.goto(-50, -290)

    def create_simple_copy(self):
        """
        Creates a SimpleGrid()-instance with the needed parameters.
        """
        copy = SimpleGrid(self.mademoves, self.boxes, self.connections, self.turn, self.greenscore, self.redscore)
        return copy


    def rendergrid(self):
        """
        Renders the graphics
        for the game and useful
        parameters to play.
        """

        # Calculates gridsize:
        if self.width > self.height:
            self.linelength = 500 / (self.width - 1)
        else:
            self.linelength = 500 / (self.height - 1)

        self.midlength = (math.sqrt((self.linelength ** 2.0) + (self.linelength ** 2))) / 2


        turtlespecs(self.t)

        # Paint all dots in turtle:
        start = [-250, 250]
        for i in range(self.height):
            lis = []
            for i in range(self.width):
                self.t.goto(start)
                self.t.dot(15)
                lis.append(tuple(start))
                start[0] += self.linelength
            start[0] = -250
            start[1] -= self.linelength
            self.dots.append(lis)

        # Create control-key dictionary:
        c = 0
        for i in range(self.height):
            for h in range(self.width-1):
                c += 1
                h_line = self.dots[i][h], self.dots[i][h+1]
                self.connections[c] = h_line
            for v in range(self.width):
                c += 1
                try:
                    v_line = self.dots[i][v], self.dots[i+1][v]
                    self.connections[c] = v_line
                except:
                    break

        # Paint all control-key labels in turtle:
        for key in self.connections:
            val = self.connections[key]
            x = (val[0][0] + val[1][0]) / 2
            y = (val[0][1] + val[1][1]) / 2
            self.t.goto(x, y)
            self.t.write(str(key), font=("Arial", 12, "normal"))

        # Create dictionary with boxes
        start = 1
        label = 0
        lines_width = self.width-1
        lines_height = self.height-1
        for i in range(lines_height):
            for u in range(lines_width):
                label += 1
                self.boxes[label] = [start]
                for e in range(2):
                    self.boxes[label].append(start+self.width-e)
                self.boxes[label].append(start+self.width*2-1)
                start += 1
            start += self.width


    def get_moves(self):
        """
        Returns a list of moves that are available in the Grid.
        """
        lis = []
        for key in self.connections:
            if key not in self.mademoves:
               lis.append(key)
        return lis


    def rendermove(self, key):
        """
        Renders the move no. (key) in the grid.
        Checks if someone gets a score and int that case
        render the proper graphics.
        """

        # Checks so the user gives the correct input.
        while key in self.mademoves or not 0 < key <= len(self.connections):
            key = int(input('Not a valid move..\n>> '))

        # Renders the graphic of a certain move.
        self.t.goto(self.connections[key][0])
        turtlespecs(self.t, speed=4, clr=self.turn, pu=False)
        self.t.width(2)
        self.t.goto(self.connections[key][1])
        turtlespecs(self.t, clr=self.turn, speed=0)
        self.mademoves.append(key)

        # Chekcs if here is a box created after the move.
        if self.is_there_box():

            # The found box is rendered
            while self.del_boxes:
                box = self.del_boxes.pop()
                self.t.goto(self.connections[box[0]][0])
                self.t.setheading(310)
                self.t.fd(self.midlength)
                self.t.pd()
                self.t.write(self.turn[0].upper(), font=("Arial", 16, "normal"))
                self.t.pu()

                # The count of the scoring is rendered.
                self.render_score(self.turn)

            # The function returns without changing the turn of the players.
            return

        # If no box is found the turn is shifted to the other player.
        if self.turn == 'green':
            self.turn = 'red'
        else:
            self.turn = 'green'


    def is_there_box(self):
        """
        Checks if there is a box drawn in the grid and returns a bool.
        """
        to_del = []
        for key in self.boxes:
            count = 0
            for line in self.boxes[key]:
                if line in self.mademoves:
                    count += 1
            if count == 4:
                to_del.append(key)
        if to_del:
            for key in to_del:
                self.del_boxes.append(self.boxes[key])
                del self.boxes[key]
            return True
        return False


    def isGameOver(self):
        """
        If there are no moves left in the grid, game is over.
        """
        if not self.get_moves():
            return True
        return False


    def whoWon(self):
        """
        Counts the score and returns who won.
        """
        if self.greenscore > self.redscore:
            return 'green'
        if self.greenscore == self.redscore:
            return 'nobody'
        return 'red'


    def evaluate(self, player):
        """
        Evaluates the score for one player
        after the outcome of the game
        """
        if not self.isGameOver():
            return None
        if self.whoWon() == player:
            return 1
        if self.whoWon() == 'nobody':
            return 0
        return -1


    def render_score(self, clr):
        """
        Renders the score of the player who got the score.
        """
        if clr == 'green':
            self.greenscore += 1
            self.gscore_turtle.undo()
            turtlespecs(self.gscore_turtle, clr=clr)
            self.gscore_turtle.goto(-150, 270)
            self.gscore_turtle.write('Green: %s' % (self.greenscore), font=("Arial", 16, "normal"))
        else:
            self.redscore += 1
            self.rscore_turtle.undo()
            turtlespecs(self.rscore_turtle, clr=clr)
            self.rscore_turtle.goto(100, 270)
            self.rscore_turtle.write('Red: %s' % (self.redscore), font=("Arial", 16, "normal"))


    def render_verbose(self, undo=False):
        """
        A small function to render a
        message in turtle saying "AI is thinking.."
        If undo=True the function will
        undo the latest action of the turtle,
        so the message can be taken away.
        """
        if undo:
            self.verboseturtle.undo()
            return
        self.verboseturtle.write('AI Thinking..', font=("Arial", 16, "normal"))