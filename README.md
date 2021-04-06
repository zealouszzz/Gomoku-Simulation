running instructions
environments: python 3.8.1
baseline battle: select the code segment in main() of battle.py and run
man vs machine: run main() of start_gomoku.py and follow the instruction to play
documents clarification
baseline algorithms: alpha_beta_pruning.py, greedy.py, minimax.py, heuristic.py
customized algorithms: enhanced_minimax.py
game status check: status.py
pattern discovery and score function: pattern_search.py
man vs machine model: start_gomoku.py
test for function and syntax: sandbox.py, function_test.py
baseline algorithms
alpha_beta_pruning
minimax
heuristic
greedy

input/output
input:
1. board -> 1515 2-D array
contains only 3 possible integers:
black token: 2
white token: 1
blank/null: 0
2. isBlack -> True(black token)/False(white token)
3. chessCount -> number of chess on the current board
4. k -> max depth of search, only used in minimax and alpha_beta_pruning
output:
board -> 1515 2-D array

customized algorithm:
input/output: same as baseline algorithms

status of board
check(board, isBlack, chessCount)
input: 1. board -> 15*15 2-D array
contains only 3 possible integers:
black token: 2
white token: 1
blank/null: 0
2. isBlack -> True(black token)/False(white token)
3. chessCount -> number of chess on the current board

output:
1 -> white wins
2 -> black wins
0 -> game is still going
-1 -> draw

score function & pattern discovery
pattern definiation(22 patterns total):
p1 = color * 5
p2 = blank + color * 4 + blank
p3= rival + color * 4 + blank
p4 = blank + color * 3 + blank + color + blank
p5 = blank + color * 2 + blank + color*2 + blank
p6 = blank + color * 3 + blank
p7 = blank + color * 2 + blank + color + blank
p8 = rival + color * 3 + blank
p9 = rival + color * 2 + blank + color + blank
p10 = rival + color + blank + color * 2 + blank
p11 = blank + color * 2 + blank * 2 + color + blank
p12 = blank + color + blank + color + blank + color + blank
p13 = rival + blank + color * 3 + blank + rival
p14 = blank + color * 2 + blank
p15 = blank * 2 + color + blank + color + blank * 2
p16 = rival + color * 2 + blank
p17 = blank + color + blank
p18 = rival + color
p19 = rival * 4 + color
p20 = blank + rival * 3 + color
p21 = blank + rival * 2 + color
p22 = rival * 2 + color + rival

score of pattern:
1:1000000, 2:50000, 3:15000, 4:15000, 5:8000,
6:15000, 7:5000, 8:4000, 9:3000, 10:3000,
11:2000, 12:2000, 13:2000, 14:1500, 15:1000,
16:500, 17:300, 18:500,19:100000,20:100000,21:1000,22:100000

score calculation depends on specific algorithm

baseline algorithms evaluation protocol
battle interface:
battles(f1,f2,record)
f1, f2 -> selected algorighms to battle(f1 holds black, f2 holds white)
record -> dict records the winner

battle protocol of two algotithms f1, f2:
let f1 holds black, f2 holds white, battle 100 times
(call battles(f1,f2, record) for 100 times)
Then let f2 holds black, f1 holds white, battle 100 times
(call battles(f2,f1,record) for 100 times)

multiprocessBattle:
To save running time, multiprocessBattle can be used for battle of two algorthms.

running time:
let selected algorithm battle with itself for 5 times,
count total steps and total running time, then calculate
average running time of each step

running results of baseline battle
success rate
heuristic vs greedy -> 106 : 94
alpha_beta_pruning vs minimax -> 31 : 19
heuristic vs alpha_beta_pruning -> 17 : 33
enhanced_alpha_beta_pruning vsalpha_beta_pruning -> 27 : 23
running time
heuristic -> 0.73 second per step
greedy -> 0.05 second per step
alpha_beta_pruning -> 79.52 second per step
minimax -> 9.69 second per step
enhanced_alpha_beta_pruning -> 9.51 second per step
man vs machine model:
select one of the five algorithms to battle
enter the postition to place your chess(by default, AI plays first and holds black)
