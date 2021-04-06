from pattern_search import huristic_score
from collections import defaultdict
import random

# construct the method here
# black = 2, white = 1, null = 0
def _heuristic(board, isBlack, chessCount,k):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
        return board

    positions = defaultdict(list)
    max_score = -1
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                cur_score = huristic_score(board, i, j, isBlack)
                positions[cur_score].append((i,j))
                if cur_score > max_score:
                    max_score = cur_score

    index = random.randint(0,len(positions[max_score])-1)
    x, y = positions[max_score][index]
    board[x][y] = chess
    return board


def main():
    pass

if __name__ == '__main__':
    main()
