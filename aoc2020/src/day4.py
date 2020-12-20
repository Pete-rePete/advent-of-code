from aoc2020.src import utils
import re

def parse_str(passports):
    psps = []
    s = passports.split('\n\n')
    s = [l.replace('\n', ' ').split(' ') for l in s]
    for l in s:
        psps.append({})
        for e in l:
            k,v = e.split(":")
            psps[-1][k] = v
    return psps

def num_limits(s, limits):
    # s: [str], limits: [list]
    try:
        i = int(s)
        if limits[0] <= i <= limits[1]:
            return True
    except:
        pass
    return False
    
def part_a(passports):
    needs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_is = []
    for i,pspt in enumerate(passports):
        good = True
        for need in needs:
            if need not in pspt:
                good=False
        x = valid_is.append(i) if good else 0
    return [passports[i] for i in valid_is]


def part_b(passports):
    psps = part_a(passports)
    # define tests
    tests = {'byr':lambda x: num_limits(x, [1920, 2002]), 
             'iyr':lambda x: num_limits(x, [2010, 2020]), 
             'eyr':lambda x: num_limits(x, [2020, 2030]), 
             'hgt':lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
                              (x.endswith("in") and 59 <= int(x[:-2]) <= 76), 
             'hcl':lambda x: bool(re.match(r"^#[\da-f]{6}$", x)), 
             'ecl':lambda x: x in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']), 
             'pid':lambda x: bool(re.match(r"^\d{9}$", x))}
    # run tests and filter out invalid passports
    valid_is = []
    for i, psp in enumerate(psps):
        good = True
        for key,test in tests.items():
            if not test(psp[key]):
                good = False
                print('failed on ',key, "'",psp[key],"'")
        x = valid_is.append(i) if good else 0
    print('valid passports:', len(valid_is))
    return [psps[i] for i in valid_is]

if __name__=='__main__':
    s = utils.data(4)
    passports = parse_str(s)
    print("Part A")
    result = part_a(passports)
    print('valid passports', len(result))
    print('part B')
    part_b(passports)
