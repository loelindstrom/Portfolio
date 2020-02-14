import tkinter as tk                # python 3
from PIL import Image, ImageTk

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
        self.textvar = tk.StringVar()
        self.label = tk.Label(self, textvariable=self.textvar)
        # self.label = tk.Label(self, textvariable=self.textvar, width=18, height=10)
        # self.textvar.set(self.controller.valueMap)
        # self.label.grid(sticky=tk.E)
        self.label.pack(fill="both", expand=True)
        # self.label.pack_propagate(0)