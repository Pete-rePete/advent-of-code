from collections import defaultdict

def fill_line(p1, p2):
    points = []
    if p1[0] == p2[0] or p1[1] == p2[1]:
        i = p1[1] == p2[1] # True corresponds with fixed value at index 1, False means index 0
        fixed = p1[i] # the dimension that remains constant is the other one
        for n in range(min(p1[~i],p2[~i]), max(p1[~i],p2[~i])+1):
            point = (n, fixed) if i else (fixed, n)
            points.append(point)
    else: # Diagonals
        xDiff, yDiff = p2[0] - p1[0], p2[1] - p1[1]
        x,y = p1
        xSign, ySign = xDiff / abs(xDiff), yDiff / abs(yDiff)
        if xSign < 0 or ySign < 0:
            pass
        for n in range(abs(xDiff) + 1):
            points.append((int(x),int(y)))
            x += xSign
            y += ySign
    return points

def part_a(coords):
    print("part A")
    lines = defaultdict(int)
    for p1,p2 in coords:
        points = fill_line(p1,p2) if (p1[0] == p2[0] or p1[1] == p2[1]) else []
        for point in points:
            lines[point] += 1
    crosses = 0
    for _,v in lines.items():
        if v > 1:
            crosses += 1
    return crosses


def part_b(coords):
    print("part B")
    lines = defaultdict(int)
    for p1,p2 in coords:
        points = fill_line(p1,p2)
        for point in points:
            lines[point] += 1
    crosses = 0
    for p,v in lines.items():
        if v > 1:
            crosses += 1
    return crosses
    
if __name__=='__main__':
    # Day 4 was pretty unconventional data format. Don't see it being reused, 
    #   so just doing data parsing here directly rather than in utils
    coordMaker = lambda l: [[int(z) for z in x.split(',')] for x in l.split(" -> ")]
    with open('aoc2021/data/day5', 'r') as f:
        coords = [coordMaker(l.strip()) for l in f.readlines()]

    print(part_a(coords))
    print(part_b(coords))
