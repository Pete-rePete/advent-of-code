from aoc2020.src import utils
from collections import defaultdict, deque
import re

def parse_rules(data):
    rules = {}
    for rule in data:
        subject = re.match('^(.*?) bags', rule).groups()[0]
        obj_pos = len(subject) + len(' bags contain ') - 1
        objects = [x.split(' ', 1) for x in re.findall(r'(\d+ .*?) bags?', rule[obj_pos:])]
        objects = [(int(n), s) for n, s in objects]
        rules[subject] = objects
    return rules

def parse_reverse_rules(data):
    reverse_rules = defaultdict(set)
    for rule in data:
        subject = re.match('^(.*?) bags', rule).groups()[0]
        obj_pos = len(subject) + len(' bags contain ') - 1
        objects = [x.split(' ', 1) for x in re.findall(r'(\d+ .*?) bags?', rule[obj_pos:])]
        for _, obj in objects:
            reverse_rules[obj].add(subject)
    return reverse_rules

def part_a(rules, my_bag):
    count = 0
    seen = set()
    rrules = parse_reverse_rules(rules)
    q = deque(rrules[my_bag])
    while q:
        bag = q.pop()
        if bag in seen:
            continue
        count += 1
        if rrules[bag]:
            q.extend(rrules[bag])
        seen.add(bag)
    return count
 
def part_b(rules, my_bag):
    rules = parse_rules(rules)
    q = deque(rules[my_bag])
    count = 0
    while q:
        n, bag = q.pop()
        count += n
        for num, sub_bag in rules[bag]:
            q.append((n * num, sub_bag))
    return count

if __name__=='__main__':
    data = utils.data(7)
    print("Part A")
    print(part_a(data, "shiny gold"))
    print('part B')
    print(part_b(data, "shiny gold"))



