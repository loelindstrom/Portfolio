import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
import numpy as np

from PIL import Image, ImageTk

# Save for later JIC:
# self.grid_slaves(row=new_row, column=new_column)[0]

class GridApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        '''

        :param args:
        :param kwargs:
        '''
        # Inherit the tk.Tk init
        tk.Tk.__init__(self, *args, **kwargs)

        # Frame which will contain the world
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        # The Grid world
        self.gridWorld = GridWorld(parent=container, controller=self, size=(3, 4))
        self.gridWorld.grid()


class GridWorld(tk.Frame):
    def __init__(self, parent, controller, size):
        '''

        :param parent:
        :param controller:
        :param size: tuple(rows, columns).
        '''
        # Inherit tk.Frame-initiation
        tk.Frame.__init__(self, parent)

        # Create reference to the root - tk.Tk
        self.controller = controller

        # Create reference to master/parent window
        self.parent = parent

        # Render the world
        self.renderWorld(rows=size[0], columns=size[1])

        # Create obstacle in world at (row, column):
        self.renderWall(1, 1)

        # Render Semla reward at (row, column)
        self.renderSemla(0, 3)

        # Create and render the agent
        self.agent = Agent(start_state=(0, 0), parent=self)
        self.agent.render()

        # Bind the arrow-keys to the control-window
        for cmd in ["<Up>", "<Down>", "<Left>", "<Right>"]:
            self.controller.bind(cmd, self.move_agent)

    def renderWorld(self, rows, columns):
        '''
        Creates a matrix with all possible states in the world.
        The matrix is a 2d-version of the same size as the world itself
        :param rows:
        :param columns:
        :return:
        '''
        self.all_States = []
        for row_index in range(rows):
            row = []
            for column_Index in range(columns):
                poss_actions = self.possibleActions(row_index, column_Index, rows, columns)

                state = State(self, self.controller, (row_index, column_Index), poss_actions,
                              bd=1, relief="ridge", width=100, height=100)
                row.append(state)
                state.grid(row=row_index, column=column_Index)
            self.all_States.append(row)

    def renderWall(self, row, column):
        '''

        :param row:
        :param column:
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
        return

    def renderSemla(self, row, column):
        '''

        :param row:
        :param column:
        :return:
        '''
        semla_state = self.all_States[row][column]
        self.image = Image.open("GridWorld/semla.jpeg")
        self.image = self.image.resize((92, 92), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.semla = tk.Label(semla_state, image=self.photo)
        self.semla.pack()

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


class State(tk.Frame):
    def __init__(self, parent, controller, index, possible_actions, **kwargs):
        '''

        :param parent:
        :param controller:
        :param index:
        :param possible_actions:
        :param kwargs:
        '''
        tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.controller = controller
        self.possible_actions = possible_actions


class Agent():
    def __init__(self, start_state, parent):
        '''

        :param start_state:
        :param parent:
        '''
        self.current_state = start_state
        self.parent = parent

        # self.image = Image.open("GridWorld/me.png")
        self.image = Image.open("GridWorld/me.png")
        self.image = self.image.resize((92, 92), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)

    def render(self):
        '''

        :return:
        '''
        agent_row = self.current_state[0]
        agent_column = self.current_state[1]
        state_of_agent = self.parent.all_States[agent_row][agent_column]
        self.agentPic = tk.Label(state_of_agent, image=self.photo)
        self.agentPic.pack()

    def move_agent(self, new_state):
        '''

        :param new_state:
        :return:
        '''
        self.current_state = new_state


if __name__ == "__main__":
    app = GridApp()
    app.mainloop()