import tkinter as tk                # python 3
from PIL import Image, ImageTk

from GWState import State
from GWAgent import Agent



class GridWorld(tk.Frame):
    def __init__(self, parent, controller, size, mode):
        """
        The place where the magic happens.
        The visualizations come true
        The place to freeroam
        The graphics of the gridworld
        :param parent: Frame which everything takes place in. Type = tk.Frame
        :param controller: Where the parent frame is situated. Type = tk.TK
        :param size: How big the world is, rows, columns. Type = tuple
        :param mode: If an agent should be able to walk around or if visualizing value iteration
                     Type = String
        """
        # Inherit tk.Frame-initiation
        tk.Frame.__init__(self, parent)

        # Keep mode to use in function:
        self.mode = mode

        # Create reference to the root - tk.Tk
        self.controller = controller

        # Create reference to master/parent window
        self.parent = parent

        # Render the world
        self.size = size
        self.renderWorld(rows=size[0], columns=size[1])

        # Create obstacle in world at (row, column):
        self.renderWall(1, 1)

        # Render Semla reward at (row, column)
        self.renderSemla(0, 3)

        # Render Fire-reward(punishment) at (row, column):
        self.renderFire(1,3)

        # If freeroaming mode: Create and render the agent
        if mode == "freeroam":
            self.agent = Agent(start_state=(0, 0), parent=self)
            self.agent.render()

        # Bind the arrow-keys to the control-window
        for cmd in ["<Up>", "<Down>", "<Left>", "<Right>"]:
            self.controller.bind(cmd, self.move_agent)

    def renderWorld(self, rows, columns):
        '''
        Creates a matrix with all possible states in the world.
        The matrix is a 2D-version of the same size as the world itself
        :param rows:
        :param columns:
        :return:
        '''
        self.all_States1D = []
        self.all_States = []
        for row_index in range(rows):
            row = []
            for column_Index in range(columns):
                poss_actions = self.possibleActions(row_index, column_Index, rows, columns)

                state = State(self, self.controller, (row_index, column_Index), poss_actions,
                              bd=1, relief="ridge", width=100, height=100)
                if self.mode == "valueiteration":
                    state.textvar.set(self.controller.valueMap[row_index, column_Index])
                self.all_States1D.append(state)
                row.append(state)
                # state.grid_propagate(False)
                state.pack_propagate(0)
                state.grid(row=row_index, column=column_Index)
            self.all_States.append(row)

    def renderWall(self, row, column):
        '''
        Renders a wall at coordinates (row, column)
        :param row: int
        :param column: int
        :return:
        '''
        obstacle_state = self.all_States[row][column]
        opposite_actions_dic = {"Up":"Down", "Down":"Up", "Left":"Right", "Right":"Left"}
        print(obstacle_state.possible_actions)
        for i, action in enumerate(obstacle_state.possible_actions):
            print(i, action)
            if action == "n/a":
                continue
            else:
                row_index, column_index = self.move(row, column, action)
                neighbour_state = self.all_States[row_index][column_index]
                index_of_replacement = neighbour_state.possible_actions.index(opposite_actions_dic[action])
                neighbour_state.possible_actions[index_of_replacement] = "n/a"
                print("NB-pa:", neighbour_state.possible_actions)
        obstacle_state.config(bg="black")
        obstacle_state.label.config(bg="black")
        return

    def renderSemla(self, row, column):
        '''

        :param row:
        :param column:
        :return:
        '''
        semla_state = self.all_States[row][column]
        self.semla_image = Image.open("GWdiv/semla.jpeg")
        self.semla_image = self.semla_image.resize((92, 92), Image.ANTIALIAS)
        self.semla_photo = ImageTk.PhotoImage(self.semla_image)
        self.semla = tk.Label(semla_state, image=self.semla_photo)
        self.semla.pack()

    def renderFire(self, row, column):
        '''

        :param row:
        :param column:
        :return:
        '''
        fire_state = self.all_States[row][column]
        self.fire_image = Image.open("GWdiv/fire.jpg")
        self.fire_image = self.fire_image.resize((92, 92), Image.ANTIALIAS)
        self.fire_photo = ImageTk.PhotoImage(self.fire_image)
        self.fire = tk.Label(fire_state, image=self.fire_photo)
        self.fire.pack()

    def move_agent(self, event):
        '''

        :param event:
        :return:
        '''
        print(event.keysym)

        current_row = self.agent.current_state[0]
        current_column = self.agent.current_state[1]
        state = self.all_States[current_row][current_column]

        if event.keysym in state.possible_actions:
            new_row, new_column = self.move(current_row, current_column, event.keysym)

            print(self.agent.current_state, "New state: ", new_row, new_column)
            self.agent.current_state = (new_row, new_column)

            self.agent.agentPic.destroy()
            self.agent.agentPic = tk.Label(self.all_States[new_row][new_column],
                                     image = self.agent.photo)
            self.agent.agentPic.pack()

    @staticmethod
    def possibleActions(row_i, column_i, rows, columns):
        '''
        Checks which actions are possible in a certain state
        and attaches these actions to that state.

        States:
        n = north, s = south, w = west, e = east

        All the states which are by the side of the world will have
        their respetive side-action removed and replaced with n/a.

        :param row_i: Int with row index of state
        :param column_i: Int with column index of state
        :param rows: Int with no. of rows
        :param columns: Int with no. of columns
        :return: List with all possible actions for the particular state which is created
        '''
        poss_actions = ["Up", "Down", "Left", "Right"]
        if row_i == 0:
            poss_actions[0] = "n/a"
        if row_i == rows - 1:
            poss_actions[1] = "n/a"
        if column_i == 0:
            poss_actions[2] = "n/a"
        if column_i == columns - 1:
            poss_actions[3] = "n/a"
        return poss_actions

    @staticmethod
    def move(row, column, keysym):
        '''

        :param row:
        :param column:
        :param keysym:
        :return:
        '''
        if keysym == "Up":
            return row-1, column
        if keysym == "Down":
            return row+1, column
        if keysym == "Left":
            return row, column-1
        if keysym == "Right":
            return row, column+1
        # return row, column
