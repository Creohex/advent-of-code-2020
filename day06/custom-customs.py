from functools import reduce
from operator import or_, and_

def groups():
    raw = [_.strip() for _ in open("input").readlines()]
    group = []

    for line in range(len(raw)):
        votes = set()
        for char in raw[line]:
            votes.add(char)
        if votes:
            group.append(votes)
        if not raw[line] or line == len(raw) - 1:
            yield list(group)
            group = []

print(sum(map(lambda votes: len(reduce(or_, votes)), groups())))
print(sum(map(lambda votes: len(reduce(and_, votes)), groups())))
