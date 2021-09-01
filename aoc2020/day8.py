from aoc2020.src import utils

def part_a(data):
    seen = set()
    line = 0
    acc = 0
    while True: 
        s = data[line]
        if line in seen:
            return acc, False
        seen.add(line)
        if s.startswith('acc'):
            acc += int(s.split()[1])
            line += 1
        elif s.startswith('jmp'):
            line += int(s.split()[1])
        else:
            line += 1
        if line >= len(data):
            return acc, True
 
def part_b(data):
    for i, s in data.items():
        instr = s[:3]
        if instr in {'nop','jmp'}:
            if instr == 'nop ':
                data[i] = 'jmp ' + s.split()[1]
            elif instr == 'jmp':
                data[i] = 'nop ' + s.split()[1]
            acc, success = part_a(data)
            if success:
                return acc
            else:
                data[i] = s

def sample():
    s = '''
            nop +500
            acc +1
            jmp +4
            acc +3
            jmp -3
            acc -99
            acc +1
            jmp -4
            acc +6
        '''.split('\n')
    return [x.strip() for x in s]

if __name__=='__main__':
    data = utils.data(8)
    data = {i:s for i,s in enumerate(data)}
    #data = sample()
    print("Part A")
    print(part_a(data))
    print('part B')
    print(part_b(data))



