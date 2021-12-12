from collections import defaultdict

class Fish(object):
    def __init__(self,days):
        self.days = int(days)
    def __repr__(self):
        return str(self.days)
    def another_day(self):
        if self.days == 0:
            self.days = 6
            return Fish(8)
        self.days -= 1

def part_a(nums, days=18):
    print("part A") if days == 80 else None
    fishes = [Fish(n) for n in nums]
    for _ in range(days):
        for i in range(len(fishes)):
            newFish = fishes[i].another_day()
            if newFish:
                fishes.append(newFish)
    return len(fishes)


def part_b(nums):
    print("Part B")
    # PArt A is not efficient at all. Doing it a different way.
    counts = defaultdict(int)
    for n in nums:
        counts[n] += 1
    days = 256
    for _ in range(days):
        newCounts = {x-1:counts[x] for x in range(9)}
        newCounts[6] += newCounts[-1]
        newCounts[8] = newCounts[-1]
        del newCounts[-1]
        counts = newCounts
    return sum([v for _,v in counts.items()])
    # If I was going to redo this, I think I'd just use a list and reassign values every iteration.
    # Seems even simpler and cleaner.
    
if __name__=='__main__':
    with open('aoc2021/data/day6', 'r') as f:
        nums = [int(n) for n in f.read().strip().split(',')]
    print('len of fishes ',len(nums))
    print(part_a(nums))
    print(part_b(nums))
