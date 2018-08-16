import Wumpus


def printInstructions():
    print("\nWelcome to Wumpus World")
    print("Commands: \n 'Enter Commands Here'\n")

def isValidInput(input):
    valid_inputs = ["north", "south", "east", "west", "n", "s", "e", "w", "grab", "g", "climb", "c",
                    "fire north", "fire south", "fire east", "fire west", "f n", "f s", "f e", "f w", "help"]
    input = input.strip().lower()

    return input in valid_inputs

def playMove(wump):

    move = ""
    while not isValidInput(move):
        move = input()

    move = move.strip().lower()

    performMove(move, wump)

    if wump.inMap:
        checkCell(wump)

def checkCell(wump):

    if wump.feelBreeze():
        print("You feel a breeze.")
    if wump.smellStench():
        print("You smell a terrible stench.")
    if wump.seeGlint():
        print("You see a glint of something that looks like gold.")
    if wump.hasWumpus() and wump.wumpusAlive:
        print("There is a live Wumpus here!")
        wump.playerAlive = False
    elif wump.hasWumpus() and not wump.wumpusAlive:
        print("There is a dead Wumpus here!")
    if wump.hasPit():
        print("You have fallen into a pit.")
        wump.playerAlive = False
    if not wump.feelBreeze() and not wump.smellStench() and not wump.seeGlint() and not wump.hasWumpus() and not wump.hasPit():
        print("It is very dark")

def performMove(move, wump):

    if move == "help":
        printInstructions()
    elif move == "north" or move == "n":
        wump.playerMoves += 1
        if not wump.stepNorth():
            print("You feel a bump as you walk into a wall.")
    elif move == "south" or move == "s":
        wump.playerMoves += 1
        if not wump.stepSouth():
            print("You feel a bump as you walk into a wall.")
    elif move == "east" or move == "e":
        wump.playerMoves += 1
        if not wump.stepEast():
            print("You feel a bump as you walk into a wall.")
    elif move == "west" or move == "w":
        wump.playerMoves += 1
        if not wump.stepWest():
            print("You feel a bump as you walk into a wall.")
    elif move == "grab" or move == "g":
        wump.playerMoves += 1
        if wump.grabGold():
            print("You pick up a pile of gold.")
        else:
            print("You do not pick up anything.")
    elif move == "climb" or move == "c":
        if wump.canClimb():
            print("You climb out of Wumpus World.")
            wump.inMap = False
        else:
            print("You cannot climb up from here.")
            wump.playerMoves += 1

    move = move.split()

    if (move[0] == "fire" or move[0] == "f") and wump.playerHasArrow:
        wump.playerMoves += 1
        print("You shoot an arrow.")
        direc = move[1]
        if wump.fire(direc):
            print("You hear a horrible scream.")
    elif (move[0] == "fire" or move[0] == "f") and not wump.playerHasArrow:
        wump.playerMoves += 1
        print("You try to fire but are out of arrows.")

def playGame(wump):

    checkCell(wump)
    while wump.playerAlive and wump.inMap:
        playMove(wump)
    calcScore(wump)

def calcScore(wump):
    if not wump.playerAlive:
        score = 0
    else:
        if wump.playerHasGold:
            score = 1000
        else:
            score = 100

        if not wump.playerHasArrow:
            score -= 10

        score -= wump.playerMoves

    print("\nFinal Score:", score)

def continuePlaying():

    choices = ["yes", "y", "no", "n"]

    choice_valid = False
    while not choice_valid:
        choice = input("\nWould you like to play again? ")
        choice = choice.strip().lower()
        if choice in choices:
            choice_valid = True

    return choice == "yes" or choice == "y"

def initWumpusWorld():

    continue_playing = True
    while continue_playing:
        wump = Wumpus.WumpusWorld()
        printInstructions()
        playGame(wump)
        continue_playing = continuePlaying()

def test(wump):

    print("Coords", (wump.playerRow, wump.playerCol))
    print()

    if isValidInput("a") or isValidInput("f") or isValidInput("fire n") or isValidInput("fn"):
        print("Error validating input: Input is invalid but is considered valid")
    if not isValidInput("North") or not isValidInput("help  ") or not isValidInput(" c") or not isValidInput("F W"):
        print("Error validating input: Input is valid but is considered invalid")

    for r in range(5):
        for c in range(5):
            if wump.worldmap.hasWumpus(r, c):
                print("Wumpus at", (r, c))
            if wump.worldmap.hasPit(r, c):
                print("Pit at", (r, c))
            if wump.worldmap.isGlinty(r, c):
                print("Gold at", (r, c))

    print()


initWumpusWorld()
