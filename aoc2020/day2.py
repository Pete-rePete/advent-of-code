from aoc2020 import utils
from collections import defaultdict

def parse_pwd_data(pwd_data):
    '''
    in: [list] each element similar to "8-10 n: nnknnnnznnnn"
    We parse out each element like so:
        limit: [8 10]
        char:   "n"
        pwd:    "nnknnnnznnnn"
    out:
        [
            (limit1, char1, pwd1),
            (limit2, char2, pwd2),
            etc...
        ]
    '''
    data = [x.split(' ') for x in pwd_data]
    data = [
        ([int(a) for a in x[0].split('-')],
        x[1][0],
        x[2])
        for x in data]
    return data

def bag_of_chars(s):
    bag = defaultdict(int)
    for c in s:
        bag[c] += 1
    return bag

def part_a(data):
    print('part A')
    valid_num = 0
    for limit, char, pwd in data:
        bag = bag_of_chars(pwd)
        if limit[0] <= bag[char] <= limit[1]:
            valid_num += 1
    print('valid passwords:', valid_num)

def part_b(data):
    print("Part B")
    valid_num = 0
    for pos, char, pwd in data:
        if (pwd[pos[0] - 1] == char) != (pwd[pos[1] - 1] == char):
            valid_num += 1
    print('valid passwords:', valid_num)

if __name__=='__main__':
    pwd_data = utils.data(2)
    data = parse_pwd_data(pwd_data)
    part_a(data)
    part_b(data)