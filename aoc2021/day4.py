def checkBoard(board,tracker):
    diag1 = all([board[i][i] in tracker for i in range(len(board))])
    diag2 = all([board[i][~i] in tracker for i in range(len(board))])
    horizontals = any([all([board[y][x] in tracker for x in range(len(board))]) for y in range(len(board))])
    verticals = any([all([board[y][x] in tracker for y in range(len(board))]) for x in range(len(board))])
    return any([diag1, diag2, verticals, horizontals])
    
def boardRemainingSum(board, tracker):
    board = board.copy()
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] in tracker:
                board[y][x] = 0
    return sum(sum(row) for row in board)

def part_a(drawNums,boards):
    print("part A")
    tracker = set()
    for num in drawNums:
        tracker.add(num)
        for board, boardSet in boards:
            if num in boardSet and checkBoard(board, tracker):
                return boardRemainingSum(board, tracker) * num

def part_b(drawNums,boards):
    print("part B")
    tracker = set()
    doneBoards = 0
    for num in drawNums:
        tracker.add(num)
        for board, boardSet in boards:
            if (-1 not in boardSet) and (num in boardSet) and checkBoard(board, tracker):
                doneBoards += 1
                boardSet.add(-1)
                if doneBoards == len(boards):
                    return boardRemainingSum(board, tracker) * num

if __name__=='__main__':
    # Day 4 was pretty unconventional data format. Don't see it being reused, 
    #   so just doing data parsing here directly rather than in utils
    with open('aoc2021/data/day4', 'r') as f:
        drawNums = [int(n) for n in f.readline().strip().split(',')]
        lines = f.readlines()
    intMatrix = lambda strMatrix: [[int(x) for x in y.strip().split()] for y in strMatrix] 
    boards = [intMatrix(lines[pos-4:pos+1]) for pos in range(5,len(lines),6)]
    setify = lambda board: set([x for row in board for x in row])
    boards = [[board,setify(board)] for board in boards]
    b_old = boards.copy()
    print(len(boards))
    print(part_a(drawNums,boards))
    print(part_b(drawNums,boards))
