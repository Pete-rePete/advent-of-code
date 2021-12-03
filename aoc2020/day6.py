from aoc2020 import utils
from collections import defaultdict

def unanimous(group):
    unanimous = len(group)
    votes = defaultdict(int)
    for ballot in group:
        for c in ballot:
            votes[c] += 1
    return [c for c in votes.keys() if votes[c] == unanimous]

def quorum(group):
    votes = set()
    for ballot in group:
        votes = votes.union(set(ballot))
    return votes

def part_a(groups):
    quorum_count = 0
    for group in groups:
        quorum_count += len(quorum(group))
    return quorum_count

def part_b(groups):
    quorum_count = 0
    for group in groups:
        quorum_count += len(unanimous(group))
    return quorum_count

if __name__=='__main__':
    data = utils.data(6)
    print("Part A")
    print(part_a(data))
    print('part B')
    print(part_b(data))


