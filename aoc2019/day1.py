import utils
from collections import deque

def part_a(nums):
    print("part A")
    fuel_sum = 0
    for num in nums:
        fuel_sum += num//3-2
    print(fuel_sum)

def part_b(nums):
    print("part B")
    fuel_sum = 0
    q = deque(nums)
    while q:
        fuel_amt = q.pop()//3-2
        if fuel_amt > 0:
            fuel_sum += fuel_amt
            q.append(fuel_amt)
    print(fuel_sum)

if __name__=='__main__':
    nums = utils.data(1)
    part_a(nums)
    part_b(nums)