from pattern_search import huristic_score
from collections import defaultdict
import random

# construct the method here
# black = 2, white = 1, null = 0
def _enhanced_alpha_beta_pruning(board, isBlack, chessCount,k):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
        return board
    positions = defaultdict(list)
    max_score = float('-inf')
    # count = 0
    for i,j in search_area(board):
        board[i][j] = chess
        score =  dfs(board, not isBlack, k, isBlack)
        board[i][j] = 0
        positions[score].append((i,j))
        if score > max_score:
            max_score = score
        # count += 1
        # print('evaluate ' + str(count) + ' position')
        # for r in board:
        #     print(r, end = '\n')
        # print('-------------------------------------------------')
                
    index = random.randint(0,len(positions[max_score])-1)
    x, y = positions[max_score][index]
    board[x][y] = chess
    return board

def dfs(board, isBlack, k, original_player):
    chess = 2 if isBlack else 1
    # max_score = float('-inf')
    if k == 1:
        return huristic_score(board, -1, -1, original_player)

    original = huristic_score(board, -1, -1, original_player)
    rival = huristic_score(board, -1, -1, not original_player)

    if original >= rival:
        return original
    k -= 1
    if isBlack == original_player:
        score = float('-inf')
        for x, y in search_area(board):
            board[x][y] = chess
            score = max(score, dfs(board, not isBlack, k, original_player))
            board[x][y] = 0    
    else:
        score = float('inf')
        for x, y in search_area(board):
            board[x][y] = chess
            score = min(score, dfs(board, not isBlack, k, original_player))
            board[x][y] = 0              
    return score

def search_area(board):
    output = set()
    for r in range(15):
        for c in range(15):
            if board[r][c] != 0:
                for d in direction():
                    for a, b in d:
                        i = r + a
                        j = c + b
                        if isValid(i,j) and board[i][j] == 0:
                            output.add((i,j))
                        if isValid(i+a, j+b) and board[i+a][j+b] == 0:
                            output.add((i+a,j+b))
         
    return output

# return four direction 
def direction():
    return [[[0,1],[0,-1]],[[1,0],[-1,0]],[[1,1],[-1,-1]],[[1,-1],[-1,1]]]

# return if postion is out of range
def isValid(i, j):
    return i > -1 and i < 15 and j > -1 and j < 15

def main():
    pass

if __name__ == '__main__':
    main()
