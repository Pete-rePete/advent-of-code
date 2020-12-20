from aoc2020.src import utils

def bs(fb, char):
    pos = 0
    n = 2 ** len(fb)
    for c in fb:
        n /= 2
        if c == char:
            pos += n
    return int(pos)

def get_rowcol(s):
    row = bs(s[:7], 'B')
    col = bs(s[7:], 'R')
    return {'row':row, 'col':col, 'id': row * 8 + col}

def part_a(data):
    ids = [get_rowcol(x)['id'] for x in data]
    return max(ids)

def part_b(data):
    ids = sorted([get_rowcol(x)['id'] for x in data])
    prev = ids[0]
    for id in ids:
        if id - prev > 1:
            col = (id - 1) %8 
            row = int((id - 1 - col) / 8)
            return {'row':row, 'col':col, 'id': id - 1}
        prev = id

if __name__=='__main__':
    data = utils.data(5)
    print("Part A")
    print(part_a(data))
    print('part B')
    print(part_b(data))


