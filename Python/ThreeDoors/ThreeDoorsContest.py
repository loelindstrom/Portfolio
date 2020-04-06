from random import *

class ContestRoom():
    def __init__(self, doorsN=3, rounds=10):
        self.doorsN = doorsN
        #           Wrong  Right
        self.tracker = [0, 0]
        self.guesses = ["      ^",
                        "             ^",
                        "                    ^"]

    def createClearedDoors(self, doorsN):
        doors = []
        for _ in range(doorsN):
            doors.append([" "])
        return doors

    def putPrizeBehindDoor(self, doors, knowsGameTheory):
        i = randint(0, self.doorsN-1)
        guess = randint(0, self.doorsN - 1)
        doors[i][0] = "x"
        print("             " + str(doors))
        print("1st guess:" + self.guesses[guess])

        for no in range(3):
            if no != i and no != guess:
                door2remove = no

        doors[door2remove] = "   "
        print("             " + str(doors))

        if knowsGameTheory:
            for no in range(3):
                if no != guess and no != door2remove:
                    guess = no
                    break

        print("2nd guess:" + self.guesses[guess])
        print("\n")

        if i == guess:
            self.tracker[1] += 1
        else:
            self.tracker[0] += 1

        return doors

    def runGameShow(self, rounds=1000):
        print("|          Let's start the Game Show:        |\n"
              "|                                            |\n"
              "|---------------GUESS THE DOOR---------------|\n"
              "\n"
              "This is a simulation of 'The Monty Hall Problem' (by Steve Selvin)\n"
              "\n"
              "The scenario is that you are presented with three doors:\n"
              "[[' '], [' '], [' ']]\n"
              "\n"
              "Behind one of the doors there's a prize:\n"
              "[[' '], ['x'], [' ']]\n"
              "        Prize\n"
              "\n"
              "But you don't know which door has the prize.\n"
              "Then you do your first guess of which door has the prize.\n"
              "Then one of the doors you didn't guess for and which didn't have the prize behind it, is removed\n"
              "\n"
              "Now the question is:\n"
              "Do you wanna stay with your first guess or do you want to switch door?\n"
              "PRESS 'f' for first guess or 's' for switching")

        user_input = str(input())
        while user_input != 'f' and user_input != 's':
            user_input = str(input("PRESS 'f' for first guess or 's'\n"))

        if user_input == 'f':
            knowsGameTheory = False
            tactic = "staying with first guess"
        else:
            knowsGameTheory = True
            tactic = "switching"

        for _ in range(rounds):
            doors = self.createClearedDoors(self.doorsN)
            doors = self.putPrizeBehindDoor(doors, knowsGameTheory)
        wrongs = self.tracker[0]
        rights = self.tracker[1]
        right_percent = rights/rounds
        print("|---------------FINISHED---------------|\n"
              "You're tactic (" + tactic + ") was tried for 1000 trials (see above)\n"
              "These are the results:\n"
              "Wrong: {}\n"
              "Right: {}\n"
              "Right %: {}\n"
              "\n"
              "See 'Monty Hall Problem' on wikipedia for why the switching tactic is the best."
              .format(wrongs, rights, right_percent))








CR = ContestRoom()
CR.runGameShow()