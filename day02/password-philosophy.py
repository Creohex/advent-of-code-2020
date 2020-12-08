def passwords():
    for line in open("input").readlines():
        low, high, char, passwd = line.strip().replace(":", "").replace("-", " ").split()
        yield (int(low), int(high), char, passwd)

def validate_occurences(letter_low, letter_high, letter, password):
    return letter_low <= password.count(letter) <= letter_high

def validate_positions(pos1, pos2, letter, password):
    return (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter)

print(len(filter(bool, (validate_occurences(*params) for params in passwords()))))
print(len(filter(bool, (validate_positions(*params) for params in passwords()))))
