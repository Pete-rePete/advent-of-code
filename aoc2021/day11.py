def get_data(test = False):
    daynum = __file__[-5:-3]
    with open('aoc2021/data/day'+daynum + ("_test" if test else ""), 'r') as f:
        data = [list(l.strip()) for l in f.readlines()]
    return data

class Octopus(object):
    def __init__(self, energyLevel, coords=(None,None), grid=None, flashes=0):
        self.coords = coords
        self.x, self.y = coords
        self.energyLevel = energyLevel
        self.grid = grid
        self.flashes = flashes
        self.turnNumber = 0

    def __add__(self, other):
        # Allows us to use the builtin python sum() method
        return Octopus(0, flashes=self.flashes + other.flashes)

    def __repr__(self):
        return str(self.energyLevel)

    def takeTurn(self):
        # increase emergy level by 1. 
        # evaluate flash
        self.energyLevel += 1
        self.turnNumber += 1
        self.evaluateFlash(self.turnNumber)

    def evaluateFlash(self, turnNumber):
        # if 10 or more, flash.
        # increase neighbours energy level by 1 if they haven't flashed this turn
        #   already (indicative if their power level is 0)
        if self.energyLevel > 9 and turnNumber == self.turnNumber:
            self.energyLevel = 0
            self.flashes += 1
            for neighbour in self.getNeighbours():
                neighbour.receiveFlash(turnNumber)

    def receiveFlash(self, turnNumber):
        # if power level > 0, increase power level. 
        # evaluate flash
        if self.energyLevel > 0 or turnNumber != self.turnNumber:
            self.energyLevel += 1
            self.evaluateFlash(turnNumber)

    def getNeighbours(self):
        positions = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        ylim = len(self.grid)
        xlim = len(self.grid[0])
        # don't judge
        return [self.grid[self.y+j][self.x+i] for i,j in positions if (self.y+j >=0 and self.y+j < ylim) and (self.x+i >=0 and self.x+i < xlim)]

        
def part_a(data):
    print("part A")
    # I would argue octopi is far superior plural word than octopuses.
    octopi = []
    for y in range(len(data)):
        octopi.append([])
        for x in range(len(data[0])):
            octopi[y].append(Octopus(int(data[y][x]), coords=(x,y),grid=octopi))

    for i in range(100): 
        for line in octopi:
            for octopus in line:
                octopus.takeTurn()
    print('\n'.join(str(line) for line in octopi) + '\n'*2)
    o = Octopus(0)
    bigO = sum([sum(line, o) for line in octopi], o)
    print(bigO.flashes)
    print([sum(line, o).flashes for line in octopi])
        
    
    

def part_b(incompleteStacks):
    print("Part B")
    
    
if __name__=='__main__':
    testData = get_data(test=True)
    data = get_data()
    part_a(data)
    #part_b(incompleteStacks)

    
