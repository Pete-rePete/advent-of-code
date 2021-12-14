from collections import deque

def get_data(test = False):
    daynum = __file__[-4]
    with open('aoc2021/data/day'+daynum + ("_test" if test else ""), 'r') as f:
        data = [[int(x) for x in l.strip()] for l in f.readlines()]
    return data

def checkLocalMinimum(y, x, data):
    val = data[y][x]
    if (y > 0) and data[y-1][x] <= val:
        return False
    if (y < len(data) - 1) and data[y+1][x] <= val:
        return False
    if (x > 0) and data[y][x-1] <= val:
        return False
    if (x < len(data[0]) - 1) and data[y][x+1] <= val:
        return False
    return True

def part_a(data):
    print("part A")
    '''
    find local minima, defined as "neighbours are all higher"
    '''
    dangers = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if checkLocalMinimum(y, x, data):
                dangers += 1 + data[y][x]
    return dangers

def directions(x,y,data):
    dirs = []
    if y > 0:
        dirs.append((x, y - 1))
    if (y < len(data) - 1) :
        dirs.append((x, y + 1))
    if (x > 0):
        dirs.append((x - 1, y))
    if (x < len(data[0]) - 1):
        dirs.append((x + 1, y))
    return dirs

def exploreBasin(x,y,data):
    seen = set()
    q = deque([(x,y)])
    basinSize = 0
    while q:
        x,y = q.popleft()
        if data[y][x] < 9 and (x,y) not in seen:
            basinSize += 1
            dirs = directions(x,y,data)
            q.extend(d for d in dirs if d not in seen)
        seen.add((x,y))
    return basinSize, seen

def part_b(data):
    print("Part B")
    # iterate every element looking for a basin
    # Keep list of seen
    # if you find a non-9 that hasn't been seen already, dive into the basin and explore it completely
    seen = set()
    basins = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x,y) not in seen and data[y][x] < 9:
                basinSize, basinSeen = exploreBasin(x,y,data)
                basins.append(basinSize)
                seen = seen.union(basinSeen)
            seen.add((x,y))
    basins = sorted(basins)
    return basins[-1] * basins[-2] * basins[-3]

    
if __name__=='__main__':
    testData = get_data(test=True)
    data = get_data()
    print(part_a(data))
    print(part_b(data))

    
