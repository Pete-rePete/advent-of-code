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
    id = row * 8 + col
    return {'row':row, 'col':col, 'id':id}

def part_a(data):
    rowcols = [get_rowcol(x) for x in data]
    ids = [x['id'] for x in rowcols]
    return max(ids)

def part_b(data):
    rowcols = [get_rowcol(x) for x in data]
    ids = sorted([x['id'] for x in rowcols])
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


