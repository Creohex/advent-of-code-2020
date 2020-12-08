from functools import reduce
from operator import mul

def trees():
    data = open("input").readlines()
    depth = len(data)
    width = len(data[0].strip())
    tree_map = {}

    for y, line in enumerate(data):
        for x, element in enumerate(line):
            if element == "#":
                tree_map[y] = tree_map.get(y, []) + [x]

    return depth, width, tree_map

def traverse(depth, width, tree_map, right, down):
    x = 0
    y = 0
    trees_encountered = 0

    while y < depth - 1:
        x += right
        y += down
        if x % width in tree_map[y]:
            trees_encountered += 1

    return trees_encountered

depth, width, tree_map = trees()
print(traverse(depth, width, tree_map, 3, 1))
print(reduce(mul, (traverse(depth, width, tree_map, right, down)
                   for right, down
                   in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])))
