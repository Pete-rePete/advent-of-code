def checkBoard(board,tracker):
    ''' sweep the 2 diagonals, all the verticals, and all the horizontals.
    - tracker [set] holding the numbers called
    - board [list[list[ints]]]
    '''
    diag1 = all([board[i][i] in tracker for i in range(len(board))])
    diag2 = all([board[i][~i] in tracker for i in range(len(board))])
    horizontals = any(
        [
            all(
                [board[y][x] in tracker for x in range(len(board))]
            ) for y in range(len(board))
        ]
    )
    verticals = any(
        [
            all(
                [board[y][x] in tracker for y in range(len(board))]
            ) for x in range(len(board))
        ]
    )
    return any([diag1, diag2, verticals, horizontals])
    
def boardRemainingSum(board, tracker):
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] in tracker:
                board[y][x] = 0
    return sum(sum(row) for row in board)

def part_a(drawNums,boards):
    print("part A")
    tracker = set()
    draw = 0
    setify = lambda board: set([x for row in board for x in row])
    # too slow without checking hashset. Still slow
    boards = [[a,b] for a,b in zip(boards,[setify(board) for board in boards])]
    winner = False
    while not winner:
        # Yes, we're taking heavy advantage of the fact we can trust AOC data.
        #   you can whiletrue at home kids, but dont do it at work!
        num = drawNums[draw]
        tracker.add(num)
        if draw >= 4:
            for board, boardSet in boards:
                if num in boardSet:
                    if checkBoard(board, tracker):
                        return boardRemainingSum(board, tracker) * num
                        winner = True
        draw += 1


def part_b(drawNums,boards):
    print("part B")
    return 

if __name__=='__main__':
    # Day 4 was pretty unconventional data format. Don't see it being reused, 
    #   so just doing data parsing here
    with open('aoc2021/data/day4', 'r') as f:
        drawNums = [int(n) for n in f.readline().strip().split(',')]
        lines = f.readlines()[1:]
    intMatrix = lambda strMatrix: [[int(x) for x in y.strip().split()] for y in strMatrix]
    boards = [intMatrix(lines[pos-5:pos]) for pos in range(5,len(lines),6)]
    print(part_a(drawNums,boards))
    #print(part_b(drawNums,boards))