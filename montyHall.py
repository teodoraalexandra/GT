import random


def montyHall(n, switchDoor):
    # Choose a random door for gift
    gift = random.randint(1, n)
    # Choose a random initial choice
    initialChoice = random.randint(1, n)

    if initialChoice != gift:
        decision = gift
    else:
        while True:
            decision = random.randint(1, n)
            if decision != initialChoice:
                break

    if switchDoor:
        finalChoice = decision
    else:
        finalChoice = initialChoice

    wonGame = (finalChoice == gift)

    return wonGame, initialChoice, finalChoice, gift


def simulation(k, n):
    # Keep same door. switchDoor = False
    gamesWonStrategy1 = 0
    # Change door. switchDoor = True
    gamesWonStrategy2 = 0
    for i in range(k):
        wonGame, initialChoice, finalChoice, gift = montyHall(n, False)
        if wonGame:
            gamesWonStrategy1 += 1

        wonGame, initialChoice, finalChoice, gift = montyHall(n, True)
        if wonGame:
            gamesWonStrategy2 += 1

    print("Games won for Strategy 1:", 100 * float(gamesWonStrategy1) / float(k), "%")
    print("Games won for Strategy 2:", 100 * float(gamesWonStrategy2) / float(k), "%")


simulation(10000, 100)
