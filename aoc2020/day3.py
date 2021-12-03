from aoc2020 import utils
from numpy import prod

def parse_str_list(l):
    return [[False if c == '.' else True for c in line] for line in l]

def traverse_grid(grid, x_add, y_add):
    rep = len(grid[0])
    trees = 0
    x = 0
    y = 0
    while y < len(grid):
        trees += grid[y][x%rep]
        y += y_add
        x += x_add
    return trees
    
def part_a(grid):
    print("Part A")
    trees = traverse_grid(grid, 3, 1)
    print('ran into', trees, 'trees')

def part_b(grid):
    print('part B')
    directions = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]
    results = [traverse_grid(grid, i[0], i[1]) for i in directions]
    print('Trees hit:', results)
    print('Answer:', prod(results))
    

if __name__=='__main__':
    l = utils.data(3)
    grid = parse_str_list(l)
    part_a(grid)
    part_b(grid)