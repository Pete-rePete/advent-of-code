import os
print('pythonpath!!',os.getenv("PYTHONPATH"),'\n\n')
print('\n')
from aoc2021 import utils

def part_a(nums):
    print("part A")
    prev = float('inf')
    increases = 0
    for num in nums:
        if num > prev:
            increases += 1
        prev = num
    return increases

def part_b(nums):
    print("part B")
    prev = float('inf')
    increases = 0
    for i in range(3,len(nums)):
        prev = nums[i-3] + nums[i-2] + nums[i-1]
        curr = nums[i-2] + nums[i-1] + nums[i]
        if curr > prev:
            increases += 1
    return increases
    

if __name__=='__main__':
    nums = utils.data(1)
    print(part_a(nums))
    print(part_b(nums))