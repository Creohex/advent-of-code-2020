char_map = ("B", "1"), ("F", "0"), ("R", "1"), ("L", "0")
raw = open("input").readlines()

for line in range(len(raw)):
    for char, val in char_map:
        raw[line] = raw[line].replace(char, val)

seats = [int(value, 2) for value in raw]

def part_one():
    return max(seats)

def part_two():
    sorted_seats = sorted(seats)
    return next(sorted_seats[i] + 1
                for i
                in range(len(sorted_seats))
                if sorted_seats[i + 1] != sorted_seats[i] + 1)

print(part_one())
print(part_two())
