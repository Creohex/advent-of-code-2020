from itertools import combinations

def find_error(numbers, preamble):
    check_list = list(numbers[:preamble])

    for i in range(preamble, len(numbers)):
        if not any(map(lambda c: sum(c) == numbers[i], combinations(check_list, 2))):
            return numbers[i]

        check_list.pop(0)
        check_list.append(numbers[i])

def find_subset(numbers, target):
    left = right = 0
    subset = [numbers[0]]

    while sum(subset) != target:
        if sum(subset) <= target:
            right += 1
            subset.append(numbers[right + 1])
        else:
            left += 1
            subset.pop(0)

    return subset

# part_one
numbers = tuple(int(num) for num in open("input").readlines())
invalid_number = find_error(numbers, 25)
print(invalid_number)

# part_two
subset = find_subset(numbers, invalid_number)
print(min(subset) + max(subset))
