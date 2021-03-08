X = 'X'
O = 'O'
EMPTY = ''

def initial_state():
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(EMPTY)
    return board

def player(board):
    global user
    count = 0
    for i in range(3):
        for j in range(3):
            count += (int(board[i][j] is X)-int(board[i][j] is O))
    if count>0:
        return O
    return X

def actions(board):
    arr = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                arr.append((i,j))
    return arr

def result(board, move):
    play = player(board)
    arr = actions(board)
    if move in arr:
        board[move[0]][move[1]] = play
    return board

def count(board):
    cnt = 0
    for i in range(3):
        for j in range(3):
            cnt += int(board[i][j] is not EMPTY)
    if cnt==9:
        return True
    return False

def winner(board):
    if count(board):
        return None
    play = player(board)
    if play is X:
        play = O
    else:
        play = X
    ####diagonal####
    if ((board[0][0] is board[1][1] is board[2][2] is play) or (board[0][2] is board[1][1] is board[2][0] is play)):
        return play

    ####rows####
    for i in range(3):
        b=True
        for j in range(3):
            b = b and (play is board[i][j])
        if b:
            return play

    ####columns####
    for j in range(3):
        b = True
        for i in range(3):
            b = b and (play is board[i][j])
        if b:
            return play

    return None

def terminal(board):
    t1 = count(board)
    t2 = winner(board)
    if(t1 or t2!=None):
        return True
    return False

def utility(board):
    t = winner(board)
    if t is None:
        return ''
    return t

def minmax(board, depth, alpha, beta):
    if terminal(board):
        if winner(board)!=None:
            return (2*int(winner(board)==X)-1)*(100-depth)
        return 0
    play = player(board)
    print(play)
    min_heur = 101
    max_heur = -101
    moves = actions(board)
    if play == X:
        for (i,j) in moves:
            heur = minmax(result(board, (i,j)), depth+1, alpha, beta)
            board[i][j] = EMPTY
            max_heur = max(heur, max_heur)
            alpha = max(alpha, heur)
            if alpha <= beta:
                break
        return max_heur
    else:
        for (i,j) in moves:
            heur = minmax(result(board, (i,j)), depth+1, alpha, beta)
            board[i][j] = EMPTY
            min_heur = min(heur, min_heur)
            beta = min(beta, heur)
            if alpha <= beta:
                break
        return min_heur
    return 0

def minimax(board):
    if terminal(board):
        return None
    play = player(board)
    best_pair = None
    best_for_X = -101
    best_for_O = 101
    moves = actions(board)
    for (i,j) in moves:
        board[i][j] = play
        t = minmax(board,0,0,0)
        print(t)
        board[i][j] = EMPTY
        if play is X:
            if best_for_X < t:
                best_pair = (i,j)
                best_for_X = t
        else:
            if best_for_O > t:
                best_pair = (i,j)
                best_for_O = t
    return best_pair
