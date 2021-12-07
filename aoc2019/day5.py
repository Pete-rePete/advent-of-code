import utils

def parse_instr(num):
    instr = num%100
    num = num//100
    modes = []
    while num > 0:
        modes.append(num%10)
        num = num//10
    if len(modes) < 3:
        [modes.append(0) for x in range(3-len(modes))]
    return instr, modes

def getvals(nums, args, modes, i):
    vals = []
    for j, argmode in enumerate(zip(args, modes), 1):
        arg,mode = argmode
        if mode == 0:
            vals.append(nums[nums[i+j]])
        elif mode == 1:
            vals.append(nums[i+j])
    return vals

def computer(nums):
    i = 0
    traceback = []
    while True:
        instr, modes = parse_instr(nums[i])
        if instr == 1:
            jump = 4
            vals = getvals(nums, nums[i+1:i+3], modes, i)
            val1,val2 = vals
            nums[nums[i+3]] = val1 + val2
        elif instr == 2:
            jump = 4
            vals = getvals(nums, nums[i+1:i+3], modes, i)
            val1,val2 = vals
            nums[nums[i+3]] = val1 * val2
        elif instr == 3:
            jump = 2
            vals = int(input('please enter integer code: '))
            nums[nums[i+1]] = vals
        elif instr == 4:
            jump = 2
            vals = getvals(nums, nums[i+1:i+2], modes, i)[0]
            print("OUTPUT VAL: " + str(vals))
            traceback = []
        elif instr == 5:
            jump = 0
            vals = getvals(nums, nums[i+1:i+3], modes, i)
            val1, val2 = vals
            i = val2 if val1 != 0 else i + 3
        elif instr == 6:
            jump = 0
            vals = getvals(nums, nums[i+1:i+3], modes, i)
            val1, val2 = vals
            i = val2 if val1 == 0 else i + 3
        elif instr == 7:
            jump = 4
            vals = getvals(nums, nums[i+1:i+3], modes, i)
            val1, val2 = vals
            if val1 < val2:
                nums[nums[i+3]] = 1
            else:
                nums[nums[i+3]] = 0
        elif instr == 8:
            jump = 4
            vals = getvals(nums, nums[i+1:i+3], modes, i)
            val1, val2 = vals
            if val1 == val2:
                nums[nums[i+3]] = 1
            else:
                nums[nums[i+3]] = 0
        elif instr == 99:
            break
        else:

            raise ValueError("expected 1, 2, 3, 4, or 99. Got " + str(instr) + "\n\n" + str(traceback))
        traceback.append((instr, modes, vals, i))
        i += jump
    return nums

def part_a(nums):
    print("part A")
    computer(nums)

def part_b():
    print("part B")
    # search what values of nums[1] and nums[2] produce the value 19690720 at position 0
    nums = utils.data(2)
    nums[1] = 62
    nums[2] = 55
    computer(nums)
    print(nums[0])
    print('didnt find any')

if __name__=='__main__':
    nums = utils.data(5)
    #nums = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    #        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    #        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    part_a(nums)
    #part_b()