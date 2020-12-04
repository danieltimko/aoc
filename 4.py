
def check_hgt(hgt):
    i = 0
    while i < len(hgt) and hgt[i].isdigit():
        i += 1
    unit = hgt[i:]
    value = hgt[:i]
    if unit == "cm":
        return 150 <= int(value) <= 193
    elif unit == "in":
        return 59 <= int(value) <= 76
    else:
        return False


def check_hcl(hcl):
    if hcl[0] != "#" or len(hcl) != 7:
        return False
    for c in hcl[1:]:
        if not c.isdigit() and c not in "abcdef":
            return False
    return True


def check_pid(pid):
    if len(pid) != 9:
        return False
    for c in pid:
        if not c.isdigit():
            return False
    return True


def is_valid(password):
    items = {}
    for line in password.split('\n'):
        for item in line.split(' '):
            key, value = item.split(':')
            items[key] = value
    conditions = ["byr" not in items or int(items["byr"]) < 1920 or int(items["byr"]) > 2002,
                  "iyr" not in items or int(items["iyr"]) < 2010 or int(items["iyr"]) > 2020,
                  "eyr" not in items or int(items["eyr"]) < 2020 or int(items["eyr"]) > 2030,
                  "hgt" not in items or not check_hgt(items["hgt"]),
                  "hcl" not in items or not check_hcl(items["hcl"]),
                  "ecl" not in items or not items["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                  "pid" not in items or not check_pid(items["pid"])]
    return not any(conditions)


def run():
    with open('input') as file:
        passwords = file.read().split('\n\n')
        count = 0
        for password in passwords:
            if is_valid(password):
                count += 1
        print(count)


run()
