import statistics

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

def part_a(nums, ):
    print("part A")
    center = statistics.median(nums)
    return int(sum([abs(n - center) for n in nums]))

def part_b(nums):
    print("Part B")
    fuel = lambda n: (n**2 + n) / 2
    center = int(statistics.mean(nums) + 0.5)
    # For the life of me I can't figure out why the center varies by 1 sometimes. bizarre. Don't care enough to figure it out
    centerFuel = [
        int(sum([fuel(abs(n - center-1)) for n in nums])), 
        int(sum([fuel(abs(n - center)) for n in nums])), 
        int(sum([fuel(abs(n - center+1)) for n in nums]))
    ]
    return min(centerFuel)
    
if __name__=='__main__':
    # testing a
    print('testing a')
    print(part_a([16,1,2,0,4,2,7,1,2,14]))
    print('testing b')
    print(part_b([16,1,2,0,4,2,7,1,2,14]))
    # REAL CODE
    daynum = __file__[-4]
    with open('aoc2021/data/day'+daynum, 'r') as f:
        nums = [int(n) for n in f.read().strip().split(',')]
    print('len of crabs ',len(nums))
    print(part_a(nums))
    print(part_b(nums))

    
