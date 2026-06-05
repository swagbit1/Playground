"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = 0

    for i in board:
        for j in i:
            if j != EMPTY:
                counter += 1

    if counter % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    notTaken = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                notTaken.add((i,j))
    return notTaken


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # deepCopyOfBoard = copy.deepcopy(board) # needs this to be a copy and not alter original board
    # for i in range(len(deepCopyOfBoard)):
    #     for j in range(len(deepCopyOfBoard[0])):
    #         if deepCopyOfBoard[i][j] == EMPTY:
    #             deepCopyOfBoard[i][j] = action
    #         else:
    #             raise Exception("Indicated cell is taken")
    # return deepCopyOfBoard

    deepCopyOfBoard = copy.deepcopy(board)

    i = action[0]
    j = action[1]

    curPlayer = player(board)

    if deepCopyOfBoard[i][j] == EMPTY:
        if curPlayer == X:
            deepCopyOfBoard[i][j] = X
        else:
            deepCopyOfBoard[i][j] = O
        return deepCopyOfBoard
    else:
        raise Exception("Indicated Cell is taken")
        



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i.count(X) == 3:
            return X
        
        if i.count(O) == 3:
            return O
    
    for j in range(len(board[0])):
        oCounter = 0
        xCounter = 0
        for i in range(len(board)):
            if board[i][j] == O:
                oCounter += 1
            elif board[i][j] == X:
                xCounter += 1
        if oCounter == 3:
            return O
        elif xCounter == 3:
            return X
        
    # check diagonal top left
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == X:
        return X
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == O:
        return O
    
    # check diagonal top right
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == X:
        return X
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == O:
        return O
    
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    instanceCounter = 0

    for i in board:
        for j in i:
            if j != EMPTY:
                instanceCounter += 1
        
    return True if instanceCounter == 9 or winner(board) else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # sice ill be X all the time, we can implement the min version
    if terminal(board):
        return None

    curPlayer = player(board)

    if curPlayer == X:
        return bestMaxValue(board)
    else:
        return bestMinValue(board)
    

def bestMaxValue(board):
    bestValue = -1000
    bestMaxAction = None

    for action in actions(board):
        value = minValue(result(board, action))  # was maxValue — fix here

        if value > bestValue:
            bestValue = value
            bestMaxAction = action

    return bestMaxAction


def bestMinValue(board):
    bestValue = 1000
    bestMinAction = None

    for action in actions(board):
        value = maxValue(result(board, action))  # was minValue — fix here

        if value < bestValue:
            bestValue = value
            bestMinAction = action

    return bestMinAction
# def bestMaxValue(board):
#     bestValue = -1000
#     bestMaxAction = None

#     for action in actions(board):
#         value = maxValue(result(board,action))

#         if value > bestValue:
#             bestValue = value
#             bestMaxAction = action

#     return bestMaxAction

# def bestMinValue(board):
#     bestValue = 1000
#     bestMinAction = None

#     for action in actions(board):
#         value = minValue(result(board,action))

#         if value < bestValue:
#             bestValue = value
#             bestMinAction = action
            
#     return bestMinAction

def maxValue(board):
    v = -1000

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v,minValue(result(board,action)))
    
    return v
    



def minValue(board):
    v = 1000

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v,maxValue(result(board,action)))
    
    return v
