import tkinter as tk                # python 3
from PIL import Image, ImageTk

class Agent():
    def __init__(self, start_state, parent):
        '''

        :param start_state:
        :param parent:
        '''
        self.current_state = start_state
        self.parent = parent

        # self.image = Image.open("GridWorld/me.png")
        self.image = Image.open("GWdiv/me.png")
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
