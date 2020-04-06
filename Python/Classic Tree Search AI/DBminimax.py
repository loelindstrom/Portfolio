import turtle
import random
from grid import Grid, SimpleGrid


def minimax(state, player, depth=-1, verbose=False):
    """
    A minimax-function for the game "Dots and Boxes". Recursive.
    :param state: A SimpleGrid instance.
    :param player: Which player the funciton will try to maximize the score for.
    :param depth: The search depth.
    :param verbose: Bool.
    :return: The best score of a certain move(int), the best move(int), If a bad move was detected(a bool)
    """

    # Statement to end series of recursion.
    if depth == 0 or state.isGameOver():
        return state.evaluate(player), None, False

    # Sets parameters for later use.
    moves = state.get_moves()
    # random.shuffle(moves)                   ### Uncomment to make AI play more unpredictable.
    bestMove = None
    badMove = False
    badMoves = []
    if player == 'green':
        previous_selfscore = state.greenscore
        previous_opscore = state.redscore
    else:
        previous_selfscore = state.redscore
        previous_opscore = state.greenscore

    # If it's the turn of the player the function
    # seeks to maximize the score for the player.
    if state.turn == player:
        bestValue = float('-inf')

        # Tries all available moves from the state and does a recursive call
        # upon itself to get the next moves:
        for move in moves:
            next_state = state.try_move(move)
            if verbose: print("AI considering move no: ", move)
            eval, _, bm = minimax(next_state, player, depth-1)
            if verbose: print('Move evaluation:', eval)

            # If an evaluated move is found and it's the
            # highest yet it's saved as the best value:
            if eval != None and eval != float('inf') and eval > bestValue:
                bestValue = eval
                bestMove = move

            # If a move was found that would give instant points to the opponent it is avoided:
            if verbose and bm:
                badMoves.append(move)

            # If a move which will give a higher score is found it becomes the best move:
            # (Only when there is a limited depth and another move hasn't been found)
            elif verbose and depth != -1:
                if player == 'green':
                    if next_state.greenscore > previous_selfscore:
                        bestMove = move
                else:
                    if next_state.redscore > previous_selfscore:
                        bestMove = move

        # If a bad move is found this makes sure it's not carried out:
        i = 0
        if verbose and depth != -1:
            while i < len(moves)-1 and moves[i] in badMoves:
                i += 1

        return bestValue, bestMove or moves[i], badMove

    # If it's not the turn of the player, the function
    # seeks to maximize the score for the player.
    else:
        bestValue = float('inf')
        for move in moves:
            # Tries all available moves from the state and does a recursive call
            # upon itself to get the next moves:
            next_state = state.try_move(move)
            if verbose: print("AI considering move no: ", move)
            eval, _, bm = minimax(next_state, player, depth-1)
            if verbose: print('Move evaluation:', eval)

            # If an evaluated move is found and it's the
            # lowest yet it's saved as the best value:
            if eval != None and  eval != float('-inf') and eval < bestValue:
                bestValue = eval
                bestMove = move

            # If the opponent to player(AI) gets a score it's flagged by changing badMove to True:
            elif player == 'green':
                if next_state.redscore > previous_opscore:
                    badMove = True
            elif player == 'red':
                if next_state.greenscore > previous_opscore:
                    badMove = True

        return bestValue, bestMove or moves[0], badMove


gamegrid = Grid(width=4, height=4)
gamegrid.rendergrid()
# while not gamegrid.isGameOver():                                                      ### Uncomment this...
#     gamegrid.rendermove(key=int(input(str(gamegrid.turn) + "'s turn:\n" + '>> ')))    ###  ...and   this for human vs. human
AI = 'red'
# AI = 'green'                  ### Uncomment to make AI Start
while not gamegrid.isGameOver():
    if gamegrid.turn == AI:
        gamegrid.render_verbose()
        copy = gamegrid.create_simple_copy()
        movesleft = len(copy.connections) - len(copy.mademoves)
        # ### Here you can fiddle around to change how far ahead the AI will look:
        if movesleft > 7:
            depth = 2
        else:
            depth = -1
        score, move, bm = minimax(copy, copy.turn, depth=depth, verbose=True)
        print('           AIs move is:', move)
        print('           Move score is:', score)
        print('\n')
        gamegrid.render_verbose(undo=True)
        gamegrid.rendermove(move)
    else:
        gamegrid.rendermove(key=int(input('Your Move: >> ')))                  ### Comment this and uncomment below for AI vs. AI
        # gamegrid.render_verbose()
        # copy = gamegrid.create_simple_copy()
        # movesleft = len(copy.connections) - len(copy.mademoves)
        # ### Here you can fiddle around to change how far ahead the AI will look:
        # if movesleft > 7:
        #     depth = 2
        # else:
        #     depth = -1
        # score, move, bm = minimax(copy, copy.turn, depth=depth, verbose=True)
        # print('           AI2s move is:', move)
        # print('           Move score is:', score)
        # print('\n')
        # gamegrid.render_verbose(undo=True)
        # gamegrid.rendermove(move)
print('The winner is %s! Greenscore: %s Redscore:%s' % (gamegrid.whoWon(), gamegrid.greenscore, gamegrid.redscore))


turtle.mainloop()