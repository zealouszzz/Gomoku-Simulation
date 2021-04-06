# input: board, 15 * 15 array
# output: integer  status
#           1      white wins
#           2      black wins
#           0      game is still going
#           -1      draw

def check(board, isBlack, chessCount):
    # game starts
    if chessCount == 0:
        return 0

    # define four direction
    direction = [[[0,1],[0,-1]],[[1,0],[-1,0]],[[1,1],[-1,-1]],[[1,-1],[-1,1]]]
    color = 2 if isBlack else 1

    # check all the positions
    for r in range(15):
        for c in range(15):
            # count linked chess with the same color if current position is not null
            if board[r][c] != 0:           
                color = board[r][c]
                for d in direction:
                    linkedChess = 1
                    for a, b in d:
                        i = r + a
                        j = c + b
                        while isValid(i,j) and board[i][j] == color:
                            linkedChess += 1
                            i += a
                            j += b
                    # game ends return winner
                    if linkedChess >= 5:
                        return color
                        
    # game end with draw
    if chessCount == 15 ** 2:
        return -1

    # game still going
    return 0

def isValid(i, j):
    return i > -1 and i < 15 and j > -1 and j < 15

def main():
    pass

if __name__ == '__main__':
    main()
