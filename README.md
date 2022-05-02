# GT

### Nash Equilibrium

#### Algorithm explanation

Step 1. Read from keyboard: STRATEGIES_FOR_PLAYER_ONE, STRATEGIES_FOR_PLAYER_TWO, PAYOFFS_CHOICE_RANDOM. Depending on payoffs choice, we will either choose some random values for the payoffs or enter the payoffs from keyboard.\
Step 2. Finding the dominant strategy for column player (player 2)\
    - parse the matrix on rows \
    - for each row, we choose the maximum payoff of the second player and change its boolean value to True \
    - in natural language, this will be something like: Regardless of what player 1 chooses, you, as player 2, will choose the best option (highest value) \
Step 3. Finding the dominant strategy for row player (player 1)\
    - parse the matrix on columns \
    - for each column, we choose the maximum payoff of the first player and change its boolean value to True \
    - in natural language, this will be something like: Regardless of what player 2 chooses, you, as player 1, will choose the best option (highest value) \
Step 4. With the help of the boolean values created in Step 2 & Step 3, if the cell containing payoffs has 2 True value, we have a Nash Equilibrium. 


#### Test algorithm 

Considering the following game, with following inputs:
```console
STRATEGIES_FOR_PLAYER_ONE = 2
STRATEGIES_FOR_PLAYER_TWO = 2
PAYOFFS_CHOICE_RANDOM = 'no'
1 1 6 -2 -2 6 3 3
```

The game will look like this:

| 1, 1  | 6, -2 |
|-------|-------|
| -2, 6 | 3, 3  | 

After Step 2, the payoffs 1 and 6 will be set to True for player 2.\
After Step 3, the payoffs 1 and 6 will be set to True for player 1.\
After Step 4, the program will print [1, 1], as this cell is the only one that has 2 True values.