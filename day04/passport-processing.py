import string


alphabet = string.ascii_lowercase + string.digits
hair_colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])


def passports():
    raw = open("input").readlines()
    passport = {}

    for i, line in enumerate(raw):
        line = line.strip()

        for record in line.split():
            key, value = record.split(":")
            passport[key] = value

        if not line or i == len(raw) - 1:
            yield passport.copy()
            passport = {}


def handle_err(func):
    def handler(*args):
        try:
            func(*args)
            return True
        except:
            return False

    return handler


@handle_err
def validate_birth_year(value):
    if not 1920 <= int(value) <= 2002:
        raise Exception()


@handle_err
def validate_issue_year(value):
    if not 2010 <= int(value) <= 2020:
        raise Exception()


@handle_err
def validate_expiration_year(value):
    if not 2020 <= int(value) <= 2030:
        raise Exception()


@handle_err
def validate_height(value):
    num = int(value[:-2])
    metric = value[-2:]

    if not (
        metric == "cm" and 150 <= num <= 193 or
        metric == "in" and 59 <= num <= 76
    ):
        raise Exception()


@handle_err
def validate_hair_color(value):
    if (
        not value[0] == "#" or
        len(value) != 7 or
        not all(ch in alphabet for ch in value[1:])
    ):
        raise Exception()


@handle_err
def validate_eye_color(value):
    if value not in hair_colors:
        raise Exception()


@handle_err
def validate_passport_id(value):
    int(value)

    if len(value) != 9:
        raise Exception()


@handle_err
def validate_country_id(value):
    pass


def part_one():
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    return len(filter(lambda p: not required_fields.difference(p), passports()))


def part_two():
    fields = {
        "byr": validate_birth_year,
        "iyr": validate_issue_year,
        "eyr": validate_expiration_year,
        "hgt": validate_height,
        "hcl": validate_hair_color,
        "ecl": validate_eye_color,
        "pid": validate_passport_id,
        "cid": validate_country_id,
    }
    required_fields = set(fields.keys()) - set(["cid"])
    valid_passports = 0

    for passport in passports():
        if required_fields.difference(passport):
            continue

        is_valid = True
        for field, value in passport.items():
            if not fields[field](value):
                is_valid = False
                break

        if is_valid:
            valid_passports += 1

    return valid_passports


print(part_one())
print(part_two())
