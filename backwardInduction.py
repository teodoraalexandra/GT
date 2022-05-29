import random

print('Number of rounds: ')
NUMBER_OF_ROUNDS = int(input())

if NUMBER_OF_ROUNDS % 2 != 0:
    print('Please enter an even number of rounds.')
    exit(0)

print('Random payoffs ? [yes/ no]')
PAYOFFS_CHOICE_RANDOM = input()
originalGame = [[0, 0] for i in range(NUMBER_OF_ROUNDS)]

if PAYOFFS_CHOICE_RANDOM == 'yes':
    for i in range(NUMBER_OF_ROUNDS):
        originalGame[i] = [random.randint(0, 100), random.randint(0, 100)]

if PAYOFFS_CHOICE_RANDOM == 'no':
    print('You might enter', NUMBER_OF_ROUNDS * 2, 'payoffs.')
    for i in range(NUMBER_OF_ROUNDS):
        firstPayoff = int(input())
        secondPayoff = int(input())
        originalGame[i] = [firstPayoff, secondPayoff]

# HARDCODED GAME
'''
originalGame = [[0, 0], [1, 5], [0, 2], [4, 9]]
NUMBER_OF_ROUNDS = 4
'''

game = originalGame.copy()
payoffToCompare = 0

for i in range(NUMBER_OF_ROUNDS - 1, 0, -1):
    if game[i][payoffToCompare] > game[i - 1][payoffToCompare]:
        game.pop(i - 1)
    else:
        game.pop(i)
    payoffToCompare = 1 if payoffToCompare == 0 else 0

print("Final payoff Player 1: ", game[0][0])
print("Final payoff Player 2: ", game[0][1])

index = originalGame.index(game[0])
print("Game was stopped at round: ", index + 1)
print("Game was stopped by player: ", 1 if index % 2 == 0 else 2)
