from collections import defaultdict

def get_data(test = False):
    daynum = __file__[-4]
    io = lambda x: (x[0].split(' '), x[1].split(' '))
    with open('aoc2021/data/day'+daynum + ("_test" if test else ""), 'r') as f:
        input = [io(l.strip().split(" | ")) for l in f.readlines()]
    return input

def part_a(data):
    print("part A")
    count = 0
    lens = {2,3,4,7}
    for out in [x[1] for x in data]:
        for digit in out:
            if len(digit) in lens:
                count += 1
    return count
    

def part_b(inputs):
    '''
      0:        1:          2:        3:        4:
         aaaa      ....      aaaa      aaaa      ....
        b    c    .    c    .    c    .    c    b    c
        b    c    .    c    .    c    .    c    b    c
         ....      ....      dddd      dddd      dddd
        e    f    .    f    e    .    .    f    .    f
        e    f    .    f    e    .    .    f    .    f
         gggg      ....      gggg      gggg      ....

       5:       6:        7:        8:        9:
         aaaa      aaaa      aaaa      aaaa      aaaa
        b    .    b    .    .    c    b    c    b    c
        b    .    b    .    .    c    b    c    b    c
         dddd      dddd      ....      dddd      dddd
        .    f    e    f    .    f    e    f    .    f
        .    f    e    f    .    f    e    f    .    f
         gggg      gggg      ....      gggg      gggg
        
    '''

    ''' 
    Immediately known segments: [1,4,7,8]
    - "a" comes from 7 - 1. [a]
    - "b" is the only segment that occurs 6 times [a,b]
    - "e" is the only segment that occurs 4 times [a,b,e]
    - "f" is the only segment that occurs 9 times [a,b,e,f]
    - "c" is the only other segment in 1, besides "f". [a,b,c,e,f]
    - "d" is the only unknown segment in 4 now. [a,b,c,d,e,f]
    - "g" is the only unknown segment, it identifies itself. [WE KNOW EVERYTHING]
    '''
    # data example: [['abc', 'ab', (10, all digits)], ['ab','abb','ab','ab]
    print("Part B") 
    output = 0
    for input in inputs:
        screenNums = input[0]
        numMap = {}
        segMap = {}
        # get 1,4,7,8
        get1478 = lambda x: {2:1, 3:7, 4:4, 7:8}[len(x)]
        for screenNum in screenNums:
            if len(screenNum) in {2,3,4,7}:
                num = get1478(screenNum)
                numMap[num] = screenNum
        # get "a" using the difference of 1 and 7
        screenChar = (set(numMap[7]) - set(numMap[1])).pop()
        segMap['a'] = screenChar
        # get "b", "e", and "f" because they have unique number of occurrences
        counter = defaultdict(int)
        for screenNum in screenNums:
            for c in screenNum:
                counter[c] += 1
        countChar = {v:k for k,v in counter.items()}
        segMap['b'] = countChar[6]
        segMap['e'] = countChar[4]
        segMap['f'] = countChar[9]
        # get "c", the only other segment in 1
        screenChar = (set(numMap[1]) - set(segMap['f'])).pop()
        segMap['c'] = screenChar
        # get "d", the only unknown segment in 4 (b,c,d,f)
        segMap['d'] = (set(numMap[4]) - set(segMap['b'] + segMap['c'] + segMap['f'])).pop()
        # Get the last one!!!!
        segMap['g'] = (set('abcdefg') - set(segMap.values())).pop()

        ## NOW. complete numMap.
        normalNums = [
            'abcefg',   # 0
            'cf',       # 1
            'acdeg',    # 2
            'acdfg',    # 3
            'bcdf',     # 4
            'abdfg',    # 5
            'abdefg',   # 6
            'acf',      # 7
            'abcdefg',  # 8
            'abcdfg'    # 9
        ]
        convertNumToScreen = lambda num: {segMap[c] for c in num}
        for i,v in enumerate(normalNums):
            for screenNum in screenNums:
                if set(screenNum) == convertNumToScreen(v):
                    numMap[i] = screenNum
        # FINALLY. reverse the mapping, and get the output values.
        screenMap = {''.join(sorted(v)):k for k,v in numMap.items()}
        convertToNum = lambda num: screenMap[''.join(sorted(num))] # gives real number as return val
        disp = input[1]
        output += 1000*convertToNum(disp[0]) + 100*convertToNum(disp[1]) + 10*convertToNum(disp[2]) + convertToNum(disp[3])
    return output


    
    
if __name__=='__main__':
    testData = get_data(test=True)
    # testing a
    #print(part_a(testData))
    #print('testing b')
    #print(part_b([16,1,2,0,4,2,7,1,2,14]))
    # REAL CODE
    data = get_data()
    print(part_a(data))
    print(part_b(data))

    
