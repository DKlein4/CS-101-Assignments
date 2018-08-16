import random


class OffMapError(Exception):
    def __init__(self):
        pass


class Cell(object):
    def __init__(self):
        self.hasWumpus = \
            self.hasGold = \
            self.hasPit = \
            self.hasBreeze = \
            self.hasStench = False


class Map(object):
    '''manages the entire map, assigns values to cells, reports status of map cells'''

    def __init__(self):
        grid = list()
        for j in range(5):
            row = tuple([Cell() for j in range(5)])
            grid.append(row)
        self.grid = tuple(grid)
        self.reset()

    def onGrid(self, r, c):
        if 0 <= r <= 4 and 0 <= c <= 4:
            return True
        else:
            return False

    def offGrid(self, r, c):
        return not self.onGrid(r, c)

    def isBreezy(self, r, c):
        if self.onGrid(r, c):
            return self.grid[r][c].hasBreeze
        else:
            raise OffMapError()

    def isSmelly(self, r, c):
        if self.onGrid(r, c):
            return self.grid[r][c].hasStench
        else:
            raise OffMapError()

    def isGlinty(self, r, c):
        if self.onGrid(r, c):
            return self.grid[r][c].hasGold
        else:
            raise OffMapError()

    def hasWumpus(self, r, c):
        if self.onGrid(r, c):
            return self.grid[r][c].hasWumpus
        else:
            raise OffMapError()

    def hasPit(self, r, c):
        if self.onGrid(r, c):
            return self.grid[r][c].hasPit
        else:
            raise OffMapError()

    def reset(self):
        '''this is NOT all that needs to be done'''
        goldPlaced = False
        while not goldPlaced:
            goldCoords = (random.randint(0, 4), random.randint(0, 4))
            if goldCoords != (0, 0):  # or dont contain pit if you're making that variation
                r = goldCoords[0]
                c = goldCoords[1]
                self.grid[r][c].hasGold = True
                goldPlaced = True

        wumpusPlaced = False
        while not wumpusPlaced:
            wumpCoords = (random.randint(0, 4), random.randint(0, 4))
            if wumpCoords != (0, 0):  # or dont contain pit if you're making that variation
                r = wumpCoords[0]
                c = wumpCoords[1]
                self.grid[r][c].hasWumpus = True

                if self.onGrid(r-1, c):
                    self.grid[r-1][c].hasStench = True
                if self.onGrid(r+1, c):
                    self.grid[r+1][c].hasStench = True
                if self.onGrid(r, c-1):
                    self.grid[r][c-1].hasStench = True
                if self.onGrid(r, c+1):
                    self.grid[r][c+1].hasStench = True

                wumpusPlaced = True

        pitsPlaced = False
        while not pitsPlaced:
            for r in range(5):
                for c in range(5):
                    if (r,c) != (0,0) and random.random() < 0.2:
                        self.grid[r][c].hasPit = True

                        if self.onGrid(r - 1, c):
                            self.grid[r - 1][c].hasBreeze = True
                        if self.onGrid(r + 1, c):
                            self.grid[r + 1][c].hasBreeze = True
                        if self.onGrid(r, c - 1):
                            self.grid[r][c - 1].hasBreeze = True
                        if self.onGrid(r, c + 1):
                            self.grid[r][c + 1].hasBreeze = True

            pitsPlaced = True


if __name__ == '__main__':
    try:
        raise OffMapError()
    except OffMapError:
        pass

    C = Cell()
    if C.hasWumpus or C.hasGold or \
            C.hasPit or C.hasBreeze or C.hasStench:
        print("Something wrong with initialization.")

    C.hasWumpus = True
    if not C.hasWumpus:
        print("Can't assign Wumpus value.")

    M = Map()
    if len(M.grid) != 5:
        print("Map has wrong number of rows.")

    for j in range(5):
        if len(M.grid[j]) != 5:
            print("Map row", j, "has wrong number of items.")

    for r in range(5):
        for c in range(5):
            if type(M.grid[r][c]) != Cell:
                print("Item in map grid is wrong type.")

    if not M.onGrid(1, 2):
        print("onGrid reports 1,2 as being off grid.")

    if M.onGrid(-1, 3) or M.onGrid(6, 3) or M.onGrid(2, -2) or M.onGrid(2, 10):
        print("OnGrid reports off-grid sites as being valid.")

    # test gold, wumpus, and pit placement
    j = 0
    i = 0

    for r in range(5):
        for c in range(5):
            if M.grid[r][c].hasGold:
                j += 1
            if M.grid[r][c].hasWumpus:
                i += 1
                print("Wumpus at", (r, c))
            if M.grid[r][c].hasPit:
                # print("Pit at ", (r, c))
                pass
            if M.grid[r][c].hasStench:
                print("Stench at ", (r, c))
            if M.grid[r][c].hasBreeze:
                # print("Breeze at ", (r, c))
                pass

    if j == 0:
        print("Error in reset: No gold placed.")
    elif j > 1:
        print("Error in reset:", j, "golds placed, should be 1")
    else:
        if M.grid[0][0].hasGold:
            print("Error in reset: Gold at origin.")

    if i == 0:
        print("Error in reset: No wumpus placed.")
    elif i > 1:
        print("Error in reset:", j, "wumpus' placed, should be 1")
    else:
        if M.grid[0][0].hasWumpus:
            print("Error in reset: Wumpus at origin.")

    if M.grid[0][0].hasPit:
        print("Error in reset: Pit at origin")



