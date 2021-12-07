import utils

def computer(nums):
    def add(i):
        nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
    def multiply(i):
        nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
    for i in range(0, len(nums), 4):
        if nums[i] == 1:
            add(i)
        elif nums[i] == 2:
            multiply(i)
        elif nums[i] == 99:
            break
        else:
            raise ValueError("expected 1, 2, or 99. Got " + str(nums[i]))
    return nums

def part_a(nums):
    print("part A")
    nums[1] = 12
    nums[2] = 2
    computer(nums)
    print(nums[0])

def part_b():
    print("part B")
    # search what values of nums[1] and nums[2] produce the value 19690720 at position 0
    for x in range(0,100):
        for y in range(0,100):
            nums = utils.data(2)
            nums[1] = x
            nums[2] = y
            computer(nums)
            if nums[0] == 19690720:
                print(x, y)
                break

if __name__=='__main__':
    nums = utils.data(2)
    part_a(nums)
    part_b()