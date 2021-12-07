import os
print('pythonpath!!',os.getenv("PYTHONPATH"),'\n\n')
print('\n')
from aoc2021 import utils

def part_a(instructions):
    print("part A")
    pos = [0,0]
    for instr in instructions:
        distance = int(instr.split(' ')[1])
        if instr.startswith('up'):
            pos[1] -= distance
        elif instr.startswith('down'):
            pos[1] += distance
        elif instr.startswith('forward'):
            pos[0] += distance
    return pos[0]*pos[1]

def part_b(nums):
    print("part B")
    pos = [0,0,0] # X, Depth , aim
    for instr in instructions:
        distance = int(instr.split(' ')[1])
        if instr.startswith('up'):
            pos[2] -= distance
        elif instr.startswith('down'):
            pos[2] += distance
        elif instr.startswith('forward'):
            pos[0] += distance
            pos[1] += distance * pos[2]
    return pos[0]*pos[1]
    

if __name__=='__main__':
    daynum = int(__file__[-4])
    instructions = utils.data(daynum)
    print(part_a(instructions))
    print(part_b(instructions))