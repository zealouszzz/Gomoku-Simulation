from greedy import _greedy
from alpha_beta_pruning import _alpha_beta_pruning
from heuristic import _heuristic
from minimax import _minimax
from enhanced_alpha_beta_pruning import _enhanced_alpha_beta_pruning
from status import check

def man_vs_machine_battle():
    print('Current available algorithms:' + '\n' + '1:minimax  2:alpha_beta_pruning  3:heuristic   4:greedy   5:enhanced_alpha_beta_pruning')
    name = input('please enter the number of algorithm to start battle:') 
    while name not in ('1','2','3','4','5'):
        name = input('please enter an valid number (or enter "exit" to stop):')
        if name.lower() == 'exit':
            print('game ends')
            return
    f = availableAlgorithms()[int(name)]

    board = [[0 for n in range(15)] for n in range(15)]
    isBlack = True
    chessCount = 0
    k = 2
    while (True):
        board = f(board, isBlack, chessCount,k)
        chessCount += 1
        result = check(board, isBlack, chessCount)
        for r in board:
            print(r, end = '\n')
        print('-------------------------------------------------')
        if result != 0:
            if result == -1:
                print('game end with draw')
                return
            print('AI wins!')
            return
        isBlack = not isBlack

        
        while True:
            position = input('please enter the row and column number of the chess (seperate by white space)(or enter "exit" to stop):')
            if position.lower() == 'exit':
                print('game ends')
                return
            try:
                x, y = position.split(' ')
                x = int(x)
                y = int(y)
                if isValid(x,y) and board[x][y] == 0:
                    board[x][y] = 2 if isBlack else 1
                    break
                print('the postition you enter is not valid')
            except:
                print('the postition you enter is not valid')
                continue

        chessCount += 1
        result = check(board, isBlack, chessCount)
        # for r in board:
        #     print(r, end = '\n')
        # print('-------------------------------------------------')
        if result != 0:
            if result == -1:
                print('game end with draw')
                return
            print('You win!')
            return
        isBlack = not isBlack

def isValid(i, j):
    return i > -1 and i < 15 and j > -1 and j < 15

def availableAlgorithms():
    return {1: _minimax, 2: _alpha_beta_pruning, 3: _heuristic, 4: _greedy, 5:_enhanced_alpha_beta_pruning}

def main():
    man_vs_machine_battle()

if __name__ == '__main__':
    main()
