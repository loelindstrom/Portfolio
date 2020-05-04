from PixelWorld2 import PixelWorld, PixelObject
import random

class Falling_Objects():
    def __init__(self):
        self.PW = PixelWorld()
        self.all_frames = self.PW.all_frames

        self.user = PixelObject([[10,10]])

        self.PW.renderPixelObject(self.user)

        # For making the user able to move the agent:
        self.move_dict = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}
        for cmd in ['<w>', '<a>', '<s>', '<d>']:
            self.PW.bind(cmd, lambda event, PixelObject=self.user, move_dict=self.move_dict :
                            self.PW.userMove(event, PixelObject, move_dict))



        self.falling_things = []
        self.timesteps = 1
        self.score = 0


        self.PW.renderPixelObjectList(self.falling_things)

    def game_play(self):
        if self.timesteps%3 == 0:
            if random.randint(1,2) == 2:
                possible_start_positions = list(range(0, self.PW.columns, 2))
            else:
                possible_start_positions = list(range(1, self.PW.columns, 2))

            for _ in range(int(self.PW.columns/4)):
                rndm = random.randint(0, len(possible_start_positions)-1)
                column_index = possible_start_positions.pop(rndm)
                self.falling_things.append(PixelObject([[0, column_index]]))

        to_remove = []
        dir = 'down'
        for i, object in enumerate(self.falling_things):
            for coordinates in object.pixel_coordinates:
                row, column = coordinates[0], coordinates[1]
                self.all_frames.turnoff(row, column)

            object.move(dir)

            if object.pixel_coordinates == self.user.pixel_coordinates:
                self.score -= 1
                self.PW.textVar.set(str(self.score))
                to_remove.append(i)

            elif object.pixel_coordinates[0][0] == self.PW.rows:
                to_remove.append(i)




        for i in to_remove[::-1]:
            self.falling_things.pop(i)

        self.PW.renderPixelObjectList(self.falling_things)

        self.timesteps += 1
        self.PW.after(200, self.game_play)


Game = Falling_Objects()
Game.game_play()
Game.PW.mainloop()