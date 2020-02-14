import tkinter as tk                # python 3
from PIL import Image, ImageTk
from GWorld import GridWorld
import dp_value_iteration2
import numpy as np


# Save for later JIC:
# self.grid_slaves(row=new_row, column=new_column)[0]

class GridApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        '''
        Creates the graphic controller-window (tk.Tk)
        where the rest of the graphics are generated in.
        :param args:
        :param kwargs:
        '''

        # Inherit the tk.Tk init
        tk.Tk.__init__(self, *args, **kwargs)

        # Frame for welcome message
        welcome_frame = tk.Frame(self, height=380, width=400)
        welcome_frame.pack_propagate(0)
        welcome_frame.grid(row=0, column=0, sticky="nsew")

        welcome_text = "Wow! So you actually ran my code!\n" \
                       "I'm flattered!\n\n" \
                       "The idea was to build a full-fledged visualizer for Reinforcement Learning algorithms.\n" \
                       "But it was a side project and other things in school came in between.\n" \
                       "So now you can only visualize the Value Iteration procedure of Dynamic Programming " \
                       "or freeroam with the robot to get to the Swedish Semla-bun.\n" \
                       "So well, he ain't much, but he's mine!\n\n" \
                       "(Also thanks to my teacher Rob who provided the ValueIt-code part)"

        # Make user choose mode - "Value iteration" or "Free roaming"
        self.welcome_msg = tk.Message(welcome_frame, width=400,
                                 font=("arial", 14),
                                 text=welcome_text)
        self.valueIteration_btn = tk.Button(welcome_frame, text="Value Iteration",
                                            command=lambda: self.makeGridWorld("valueiteration"),
                                            cursor="spider")
        self.freeRoam_btn = tk.Button(welcome_frame, text="Free roam",
                                      command=lambda: self.makeGridWorld("freeroam"),
                                      cursor="man")
        self.welcome_msg.pack(fill="none", expand=True)
        self.valueIteration_btn.pack(fill="none", expand=True)
        self.freeRoam_btn.pack(fill="none", expand=True)


    def makeGridWorld(self, mode):
        # Remove previous menu
        self.welcome_msg.destroy()
        self.valueIteration_btn.destroy()
        self.freeRoam_btn.destroy()

        # Frame with controls:
        control_container = tk.Frame(self, height=150)
        control_container.pack_propagate(0)
        control_container.grid(row=0, column=0, sticky="nsew")

        # Frame which will contain the world
        world_container = tk.Frame(self)
        world_container.grid(row=1, column=0, sticky="nsew")

        if mode == "valueiteration":
            # Parameters for Value iteration
            self.iteration = 0
            self.gamma = 0.9
            self.rewardSize = 0
            next_iteration_btn = tk.Button(control_container, text="Next Iteration", command=self.nexIteration)
            next_iteration_btn.pack(fill="none", expand=True)

            # Creat the Grid world
            self.valueMap = dp_value_iteration2.valueMap
            self.gridWorld = GridWorld(parent=world_container, controller=self, size=(3, 4), mode=mode)
            self.gridWorld.grid()

        if mode == "freeroam":
            self.gridWorld = GridWorld(parent=world_container, controller=self, size=(3, 4), mode=mode)
            self.gridWorld.grid()


    def nexIteration(self):
        """
        A function to see the next iteration in Value-iteration.
        :return:
        """
        self.valueMap = dp_value_iteration2.runValueIteration(gamma=self.gamma, rewardSize=self.rewardSize)
        for value, state in zip(np.nditer(self.valueMap), self.gridWorld.all_States1D):
            state.textvar.set(str(round(float(value), 3)))
        return
