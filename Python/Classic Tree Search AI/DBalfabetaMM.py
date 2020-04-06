import turtle
import random
from alfabetagrid import Grid, SimpleGrid


def minimax(state, player, depth=-1, verbose=False, alpha=float('-inf'), beta=float('inf')):

    if depth == 0 or state.isGameOver():
        return state.evaluate(player), None

    moves = state.get_moves()
    random.shuffle(moves)
    bestMove = None

    if state.turn == player:
        for move in moves:
            next_state = state.try_move(move)
            if verbose: print("AI considering move no: ", move)
            eval, _ = minimax(next_state, player, depth-1, alpha=alpha, beta=beta)
            if verbose: print('Move evaluation:', eval)
            if eval > alpha:
                alpha = eval
                bestMove = move
            if beta <= alpha:
                break
        return alpha, bestMove or moves[0]

    else:
        for move in moves:
            next_state = state.try_move(move)
            if verbose: print("AI considering move no: ", move)
            eval, _ = minimax(next_state, player, depth-1, alpha=alpha, beta=beta)
            if verbose: print('Move evaluation:', eval)
            if eval < beta:
                beta = eval
                bestMove = move
            if beta <= alpha:
                break
        return beta, bestMove or moves[0]


gamegrid = Grid(width=4, height=4)
gamegrid.rendergrid()
AI = 'red'
# AI = 'green'                  ### Uncomment to make AI Start
while not gamegrid.isGameOver():
    if gamegrid.turn == AI:
        gamegrid.render_verbose()
        copy = gamegrid.create_simple_copy()
        movesleft = len(copy.connections) - len(copy.mademoves)

        ### Here you can fiddle around to change how far ahead the AI will look:
        if movesleft > 18:
            depth = 4
        elif movesleft > 12:
            depth = 5
        elif movesleft > 7:
            depth = 6
        else:
            depth = -1

        score, move = minimax(copy, copy.turn, depth=depth, verbose=True)
        print('           AIs move is:', move)
        print('           Move score is:', score)
        print('\n')
        gamegrid.render_verbose(undo=True)
        gamegrid.rendermove(move)
    else:
        gamegrid.rendermove(key=int(input('Your Move: >> ')))                ### Comment this and uncomment below for AI vs. AI
        # gamegrid.render_verbose()
        # copy = gamegrid.create_simple_copy()
        # movesleft = len(copy.connections) - len(copy.mademoves)
        #
        # # ### Here you can fiddle around to change how far ahead the AI will look:
        # if movesleft > 18:
        #     depth = 4
        # elif movesleft > 12:
        #     depth = 5
        # elif movesleft > 7:
        #     depth = 6
        # else:
        #     depth = -1
        #
        # score, move = minimax(copy, copy.turn, depth=depth, verbose=True)
        # print('           AIs move is:', move)
        # print('           Move score is:', score)
        # print('\n')
        # gamegrid.render_verbose(undo=True)
        # gamegrid.rendermove(move)
print('The winner is %s! Greenscore: %s Redscore:%s' % (gamegrid.whoWon(), gamegrid.greenscore, gamegrid.redscore))

turtle.mainloop()