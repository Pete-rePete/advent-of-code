from collections import defaultdict

def double_digit_rule_a(num):
    num = str(num)
    return len(num) > len(set(list(num)))

def double_digit_rule_b(num):
    counts = defaultdict(int)
    while num > 0:
        counts[num%10] += 1
        num = num//10
    return any({counts[key]==2 for key in counts.keys()})

def increasing_rule(num):
    lnum  = []
    while num > 0:
        lnum.append(num%10)
        num = num//10
    prev = float('-inf')
    while lnum:
        dig = lnum.pop()
        if dig < prev:
            return False
        prev = dig
    return True

def part_a(nums):
    print("part A")
    r1 = double_digit_rule_a
    r2 = increasing_rule 
    rules = lambda n:True if r1(n) and r2(n) else False
    possibilities = [n for n in range(nums[0],nums[1]+1) if rules(n)]
    print(len(possibilities))

    
def part_b(nums):
    print("part B")
    r1 = double_digit_rule_b
    r2 = increasing_rule 
    rules = lambda n:True if r1(n) and r2(n) else False
    possibilities = [n for n in range(nums[0],nums[1]+1) if rules(n)]
    print(len(possibilities))
    

if __name__=='__main__':
    pwd_range = [183564,657474]
    part_a(pwd_range)
    part_b(pwd_range)