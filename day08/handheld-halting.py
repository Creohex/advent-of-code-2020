instructions = [(line[:3], int(line[4:])) for line in open("input").readlines()]

def run(instructions):
    visited = set()
    pos = 0
    acc = 0

    while True:
        if pos == len(instructions):
            return True, acc

        op, value = instructions[pos]

        if pos in visited:
            return False, acc
        elif pos == len(instructions):
            return True, acc

        visited.add(pos)

        if op == "nop":
            pos += 1
        elif op == "acc":
            acc += value
            pos += 1
        elif op == "jmp":
            pos += value

def part_one():
    return run(instructions)[1]

def part_two():
    for index, _ in filter(lambda i: i[1][0] in ("nop", "jmp"), enumerate(instructions)):
        edited = list(instructions)
        edited[index] = ("nop" if edited[index][0] == "jmp" else "jmp", edited[index][1])
        result, acc = run(edited)
        if result:
            return acc

print(part_one())
print(part_two())
