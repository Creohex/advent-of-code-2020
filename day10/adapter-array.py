from functools import reduce

adapters = [int(jolts) for jolts in open("input").readlines()]
adapters = sorted(adapters + [0, max(adapters) + 3])
sequence = [adapters[i + 1] - adapters[i] for i in reversed(range(len(adapters) - 1))]

def part_one():
    return sequence.count(1) * sequence.count(3)

def part_two():
    chunk_combinations = {
        2: 2,
        3: 4,
        4: 7,
    }

    return reduce(lambda a,b: a * b,
                  map(lambda s: chunk_combinations[len(s)],
                      filter(lambda s: len(s) > 1,
                              "".join(map(str, sequence)).split("3"))))

print(part_one())
print(part_two())


# sequences of 2 (2)
# 1 1
# - 1

# sequences of 3 (4)
# 1 1 1
# 1 - 1
# - 1 1
# - - 1

# sequences of 4 (7)
# 1 1 1 1
# 1 1 - 1
# 1 - 1 1
# - 1 1 1
# 1 - - 1
# - - 1 1
# - 1 - 1
