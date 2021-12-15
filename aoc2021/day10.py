def get_data(test = False):
    daynum = __file__[-5:-3]
    with open('aoc2021/data/day'+daynum + ("_test" if test else ""), 'r') as f:
        data = [l.strip() for l in f.readlines()]
    return data

def part_a(data):
    print("part A")
    openbr = set(['{','[','<','('])
    pair = {'}':'{', ']':'[', '>':'<', ')':'('}
    pointMap = {")":3, "]": 57, "}": 1197, ">": 25137}
    points = 0
    incompleteStacks = []
    for i, line in enumerate(data):
        stack = []
        badLine = False
        for c in line:
            if c in openbr:
                stack.append(c)
            else: # must be closing bracket
                if stack and pair[c] == stack[-1]:
                    stack.pop()
                else: # we have an error! add points and break)
                    points += pointMap[c]
                    badLine = True
                    break
        if badLine:
            incompleteStacks.append(stack)
    print(points)
    return incompleteStacks

    

def part_b(incompleteStacks):
    print("Part B")
    pointMap = {"(":1, "[": 2, "{": 3, "<": 4}
    scores = []
    for stack in incompleteStacks:
        lineScore = 0
        for c in stack:
            lineScore = lineScore*5 + pointMap[c]
        scores.append(lineScore)
    print(sorted(scores))
    print(sorted(scores)[len(scores)//2+1])

    
if __name__=='__main__':
    testData = get_data(test=True)
    data = get_data()
    incompleteStacks = part_a(testData)
    part_b(incompleteStacks)

    
