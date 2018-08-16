import Map

class WumpusWorld(object):

    def __init__(self):
        self.worldmap = Map.Map()
        self.wumpusAlive = True
        self.playerAlive = True
        self.inMap = True
        self.playerHasGold = False
        self.playerHasArrow = True
        self.playerMoves = 0
        self.playerRow = 0
        self.playerCol = 0

    def stepEast(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.onGrid(r, c+1):
            self.playerCol += 1
            return True
        else:
            return False

    def stepWest(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.onGrid(r, c-1):
            self.playerCol -= 1
            return True
        else:
            return False

    def stepSouth(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.onGrid(r-1, c):
            self.playerRow -= 1
            return True
        else:
            return False

    def stepNorth(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.onGrid(r+1, c):
            self.playerRow += 1
            return True
        else:
            return False

    def grab(self, r, c):
        self.worldmap.grid[r][c].hasGold = False
        self.playerHasGold = True

    def grabGold(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.isGlinty(r, c):
            self.grab(r,c)
            return True
        else:
            return False

    def fire(self, direction):
        r = self.playerRow
        c = self.playerCol
        self.playerHasArrow = False
        if direction == "n" or direction == "north":
            for i in range(r+1, 5):
                if self.worldmap.hasWumpus(i, c):
                    self.wumpusAlive = False
                    return True

            return False
        if direction == "s" or direction == "south":
            for i in range(r-1, 0, -1):
                if self.worldmap.hasWumpus(i, c):
                    self.wumpusAlive = False
                    return True

            return False
        if direction == "e" or direction == "east":
            for i in range(c+1, 5):
                if self.worldmap.hasWumpus(r, i):
                    self.wumpusAlive = False
                    return True

            return False
        if direction == "w" or direction == "west":
            for i in range(c-1, 0, -1):
                if self.worldmap.hasWumpus(r, i):
                    self.wumpusAlive = False
                    return True

            return False

    def canClimb(self):
        if self.playerRow == 0 or self.playerRow == 4 or self.playerCol == 0 or self.playerCol == 4:
            return True
        else:
            return False

    def feelBreeze(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.isBreezy(r,c):
            return True
        else:
            return False

    def smellStench(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.isSmelly(r, c):
            return True
        else:
            return False

    def seeGlint(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.isGlinty(r, c):
            return True
        else:
            return False

    def hasWumpus(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.hasWumpus(r, c):
            return True
        else:
            return False

    def hasPit(self):
        r = self.playerRow
        c = self.playerCol
        if self.worldmap.hasPit(r, c):
            return True
        else:
            return False


if __name__ == '__main__':
    w = WumpusWorld()
    if w.stepWest():
        print("Error moving West. Should be off board but is not.")
    w.stepEast()
    if w.playerCol != 1:
        print("Error stepping east")
    w.stepWest()
    if w.playerCol != 0:
        print("Error stepping west")
    if w.stepSouth():
        print("Error moving South. Should be off board but is not.")
    w.stepNorth()
    if w.playerRow != 1:
        print("Error stepping north")
    w.stepSouth()
    if w.playerRow != 0:
        print("Error stepping west")

    w.playerCol = 0
    w.playerRow = 0
    if not w.canClimb():
        print("Error Climbing: Should be able to climb but is not")
    w.stepEast()
    w.stepNorth()
    if w.canClimb():
        print("Error Climbing: Should not be able to climb but is")
    w.playerCol = 4
    w.playerRow = 4
    if not w.canClimb():
        print("Error Climbing: Should be able to climb but is not")

    count = 0
    gold_row = gold_col = 0
    for r in range(5):
        for c in range(5):
             if w.worldmap.isGlinty(r, c):
                count += 1
                gold_row = r
                gold_col = c
    if count != 1:
        print("Error more than one gold registered")
    w.playerRow = gold_row
    w.playerCol = gold_col
    if not w.seeGlint():
        print("Should see glint but do not")
    w.grabGold()
    if w.seeGlint():
        print("Should not see gold but do")

    count = 0
    wump_row = wump_col = 0
    for r in range(5):
        for c in range(5):
            if w.worldmap.hasWumpus(r,c):
                count += 1
                wump_row = r
                wump_col = c
    if count != 1:
        print("Error more than one wumpus registered")
    w.playerRow = wump_row
    w.playerCol = wump_col
    if not w.hasWumpus():
        print("Should see wumpus but do not")
    w.playerCol -= 1
    try:
        if not w.smellStench():
            print("Should smell stench but do not")
    except Map.OffMapError:
        pass
    w.playerCol -= 1
    try:
        if w.smellStench():
            print("Should smell stench but do not")
    except Map.OffMapError:
        pass

    w.playerRow = wump_row-1
    w.playerCol = wump_col
    if not w.fire("n"):
        print("Error when firing: should have hit wumpus but did not")
    if w.fire("n"):
        print("Error when firing: should not have hit wumpus but did")
    if w.fire("s"):
        print("Error when firing: should not have hit wumpus but did")
    if w.fire("w"):
        print("Error when firing: should not have hit wumpus but did")
    if w.fire("e"):
        print("Error when firing: should not have hit wumpus but did")
    if w.wumpusAlive:
        print("Error getting rid of the wumpus")
    if w.fire("n"):
        print("Error when firing: should not have hit wumpus but did")

    w.worldmap.reset()


    # print(w.playerCol)
    # for i in range(5):
    #     if w.stepEast():
    #         print(w.playerCol)
    #
    # print(w.playerRow)
    # for i in range(5):
    #     if w.stepNorth():
    #         print(w.playerRow)

    # w.playerCol = 0
    # w.playerRow = 0
    #
    # w.stepEast()
    # w.stepEast()
    # w.stepEast()
    # w.stepNorth()
    # w.stepNorth()
    # print(w.playerRow, w.playerCol)

