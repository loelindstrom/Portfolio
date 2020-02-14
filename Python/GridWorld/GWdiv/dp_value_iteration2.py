"""
Created on Thurs Nov 14 2019

@author: Robert Lowe
A value iteration example of Dynamic Programming using the grid world maze 
navigation task from Lecture 2

Modified by Loe Lindström to fit with the GWApp
"""
import numpy as np
from operator import add
import pandas as pd

############################### parameters ###########################
# gamma = 0.9#1 # discounting rate
# rewardSize = 0 # -1
gridSize = 4
terminationStates = [[0,0], [gridSize-2, gridSize-1]]   # top left and bottom right coordinates
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]            # up, down, right, left
numIterations = 100                                     # max number of iterations instead of convergence threshold
valueMap = np.zeros((gridSize-1, gridSize))             # shows state vales over the grid world

############################## rewarding/costly states in the environment (part 1, iii)
valueMap[0,3] = 1                                       # assign reward to grid pos 0,3
valueMap[1,3] = -1                                      # assign cost to grid pos 1,3

######### assign grid coordinates to all states
states = [[i, j] for i in range(gridSize-1) for j in range(gridSize)]

valueMap
deltas = []

######### assign values to unintended state transtions (alternative 'actions')
def lookUpAlternativeVals(state, action, actions, rewardSize):

    altRews = np.zeros(2)    
    vals = np.zeros(2)
    altRews[0] = rewardSize
    altRews[1] = rewardSize
    # below: alternative actions concern i) outside the environment (hit the wall?), 
    # i.e. -1 and 4 are outside the grid, 
    # ii) moving into the obstacle (position 1,1 on the grid) 
    i = 0 # count for alternative actions, maximum 2
    for actAlt in actions:
        if actAlt == action :                          # don't consider the "correct" movement
            continue
        elif list(map(add, actAlt, action)) ==  [0,0]: # calculate if the actAlt is opposite (if so, ignore)
            continue
        elif actAlt != action :
            nextState = np.array(state) + np.array(actAlt)  
            if (-1 in nextState or nextState[0] >= 3 or nextState[1] == 4
                or (nextState[0] == 1 and nextState[1]) == 1): 
                nextState = np.array(state)
                vals[i] = valueMap[state[0],state[1]] 
            else:
                vals[i] = valueMap[nextState[0], nextState[1]]
            i = i + 1
            if i>1:
                break
   
    return vals, altRews

# a function which 'moves' the agent to the next state depending on the action taken 
# and returns a reward (-1, 0 or 1)   
def actionRewardFunction(state, action, rewardSize):
    
    reward = rewardSize
    nextState = np.array(state) + np.array(action)

    if (-1 in nextState or nextState[0] >= 3 or nextState[1] == 4
        or (nextState[0] == 1 and nextState[1]) == 1): 
        nextState = state
    
    return nextState, reward 

# this is the 'main' loop where we carry out the value iteration
# for it in range(numIterations):
def runValueIteration(gamma, rewardSize):
    global valueMap
    oldValueMap = np.copy(valueMap)
    deltaState = []
    Q = np.zeros((gridSize-1, gridSize,4)) # can also calculate Q values here
    policy = np.zeros((gridSize-1, gridSize))
    for state in states:
        newV = 0
        if state == states[3] or state == states[5] or state == states[7]:
            continue
        
        actionList = np.zeros(len(actions))
        acit = -1
        for action in actions:
            acit = acit + 1
            # action index = 0(up), 1(down), 2(right), 3(left)
            nextState, reward = actionRewardFunction(state, action, rewardSize)
            
            # calculate probabilistic 'weighted' values (given alternative state transitions)
            vals,altrews = lookUpAlternativeVals(state, action, actions, rewardSize)
            # estimate bellman optimality equation through update for action taking into account
            # all state transition probabilities
            candidateV = (0.8*(reward+(gamma*valueMap[nextState[0], nextState[1]])) + 
                          0.1*(altrews[0]+(gamma*vals[0])) + 
                          0.1*(altrews[1]+(gamma*vals[1]))) 
            
            actionList[acit] = candidateV 
        newV = max(actionList)
        Q[state[0],state[1],:] = actionList # output Q in the Console window to see the result
        argMaxQ = pd.Series(Q[state[0],state[1]]).idxmax()
        policy[state[0],state[1]]= argMaxQ # improved policy
        deltaState.append(np.abs(oldValueMap[state[0], state[1]]-newV))
        oldValueMap[state[0], state[1]] = newV
        
    deltas.append(deltaState)
    valueMap = oldValueMap
    return valueMap
