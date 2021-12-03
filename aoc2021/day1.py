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
    search_set = dict()
    for x in nums:
        for y in nums:
            search_set[2020-x-y] = [x,y]
    for num in nums:
        if num in search_set.keys():
            print(num, ",", search_set[num][0],",",search_set[num][1], "are the numbers.")
            print('the answer:', num * search_set[num][0] * search_set[num][1])
            break

if __name__=='__main__':
    nums = utils.data(1)
    part_a(nums)
    #part_b(nums)