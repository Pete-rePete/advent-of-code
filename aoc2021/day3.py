import os
print('pythonpath!!',os.getenv("PYTHONPATH"),'\n\n')
print('\n')
from aoc2021 import utils

def part_a(snums):
    print("part A")
    counts = 12 * [0]
    for i in range(12):
        for s in snums:
            if s[i] == '1':
                counts[i] += 1
    gam = []
    eps = []
    for i in range(12):
        if counts[i] > len(snums)//2:
            gam.append('1')
            eps.append('0')
        else:
            gam.append('0')
            eps.append('1')
    gamma = int(''.join(gam),2)
    epsilon = int(''.join(eps), 2)
    print('PRODUCT:',gamma * epsilon)
    return gamma, epsilon


def part_b(snums):
    print("part B")
    mosts = snums.copy()
    leasts = snums.copy()
    for i in range(12):
        # MOSTS
        onecounts = 0
        if len(mosts) > 1:
            for snum in mosts:
                if snum[i] == '1':
                    onecounts += 1 
            mosti = '1' if onecounts >= (len(mosts)+1)//2 else '0'
            mosts = [snum for snum in mosts if snum[i] == mosti]
        # LEASTS
        onecounts = 0
        if len(leasts) > 1:
            for snum in leasts:
                if snum[i] == '1':
                    onecounts += 1 
            leasti = '0' if ((onecounts >= (len(leasts)+1)//2 and onecounts != len(leasts)) or onecounts == 0) else '1'
            leasts = [snum for snum in leasts if snum[i] == leasti]
    # combine
    ox = int(leasts[0],2)
    co = int(mosts[0],2)
    return ox*co

if __name__=='__main__':
    daynum = int(__file__[-4])
    snums = utils.data(daynum)
    print(part_a(snums))
    print(part_b(snums))