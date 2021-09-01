from aoc2020.src import utils

def part_a(nums):
    print("part A")
    search_set = set(2020-x for x in nums)
    for num in nums:
        if num in search_set:
            print(num, "and", 2020-num, "are the numbers.")
            print('the answer:', num * (2020-num))
            break

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
    part_b(nums)