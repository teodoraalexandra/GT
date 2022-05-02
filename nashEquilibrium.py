import random

print('Strategies for player 1: ')
STRATEGIES_FOR_PLAYER_ONE = int(input())
print('Strategies for player 2: ')
STRATEGIES_FOR_PLAYER_TWO = int(input())
print('Random payoffs ? [yes/ no]')
PAYOFFS_CHOICE_RANDOM = input()

# Hardcoded 2x2 game with one NE
'''
game = [[0] * STRATEGIES_FOR_PLAYER_ONE for i in range(STRATEGIES_FOR_PLAYER_TWO)]
game[0][0] = [[1, False], [1, False]]
game[0][1] = [[6, False], [-2, False]]
game[1][0] = [[-2, False], [6, False]]
game[1][1] = [[3, False], [3, False]]
'''

if PAYOFFS_CHOICE_RANDOM == 'yes':
    game = [[0] * STRATEGIES_FOR_PLAYER_ONE for i in range(STRATEGIES_FOR_PLAYER_TWO)]
    for i in range(STRATEGIES_FOR_PLAYER_ONE):
        for j in range(STRATEGIES_FOR_PLAYER_TWO):
            game[i][j] = [[random.randint(0, 9), False], [random.randint(0, 9), False]]

if PAYOFFS_CHOICE_RANDOM == 'no':
    print('You might enter', STRATEGIES_FOR_PLAYER_ONE * STRATEGIES_FOR_PLAYER_TWO * 2, 'payoffs.')
    game = [[0] * STRATEGIES_FOR_PLAYER_ONE for i in range(STRATEGIES_FOR_PLAYER_TWO)]
    for i in range(STRATEGIES_FOR_PLAYER_ONE):
        for j in range(STRATEGIES_FOR_PLAYER_TWO):
            firstPayoff = int(input())
            secondPayoff = int(input())
            game[i][j] = [[firstPayoff, False], [secondPayoff, False]]


# Printing game
def printGame(newGame):
    for a in range(STRATEGIES_FOR_PLAYER_ONE):
        for b in range(STRATEGIES_FOR_PLAYER_TWO):
            print(newGame[a][b], end='')
        print('\n')


def findMaxColumnIndex(payoffList):
    maxIndex = 0
    maxItem = payoffList[0][0]
    payoffIndex = 0
    for i in payoffList:
        if i[0] >= maxItem:
            maxItem = i[0]
            maxIndex = payoffIndex
        payoffIndex += 1
    return maxIndex


# Finding dominant strategy for column player
row_numbers = []
for i in range(STRATEGIES_FOR_PLAYER_ONE):
    for j in range(STRATEGIES_FOR_PLAYER_TWO):
        row_numbers.append(game[i][j][1])
    index = findMaxColumnIndex(row_numbers)
    game[i][index][1][1] = True
    row_numbers = []

# Finding dominant strategy for row player
column_numbers = []
for i in range(STRATEGIES_FOR_PLAYER_ONE):
    for j in range(STRATEGIES_FOR_PLAYER_TWO):
        column_numbers.append(game[j][i][0])
    index = findMaxColumnIndex(column_numbers)
    game[index][i][0][1] = True
    column_numbers = []

# Printing all NE (pairs of True-True)
printGame(game)
for i in range(STRATEGIES_FOR_PLAYER_ONE):
    for j in range(STRATEGIES_FOR_PLAYER_TWO):
        # For each cell, we will always have 2 values, as we have only 2 players
        if game[i][j][0][1] == True and game[i][j][1][1] == True:
            print('NE: [', game[i][j][0][0], ',', game[i][j][1][0], ']')
