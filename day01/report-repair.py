from operator import mul
from itertools import combinations
from functools import reduce

def entries(nums):
    return next(combo for combo
                in combinations(
                    map(int, open("input").read().split()),
                    nums)
                if sum(combo) == 2020)

print(reduce(mul, entries(2)))
print(reduce(mul, entries(3)))
