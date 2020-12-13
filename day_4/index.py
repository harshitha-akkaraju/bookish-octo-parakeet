filename = "input.txt"

passports = []
curr_passport = {}

filehandle = open(filename, 'r')
while True:
    line = filehandle.readline()
    if not line:
        break
    
    line = line.strip()

    if line == "":
        passports.append(curr_passport)
        curr_passport = {}
    else:
        fields = line.split(" ")
        for field in fields:
            parts = field.split(":")
            name = parts[0]
            value = parts[1]
            curr_passport[name] = value

passports.append(curr_passport)

def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # cid is not required
    for field in required_fields:
        if field not in passport:
            return False
    return True

def is_valid_passport_v2(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # cid is not required
    for field in required_fields:
        if field not in passport:
            return False
        
        value = passport[field]
        if field == "byr":
            if not year_within_range(value, 1920, 2002):
                return False
        elif field == "iyr":
            if not year_within_range(value, 2010, 2020):
                return False
        elif field == "eyr":
            if not year_within_range(value, 2020, 2030):
                return False
        elif field == "hgt":
            if not is_valid_height(value):
                return False
        elif field == "hcl":
            if not is_valid_hair_color(value):
                return False
        elif field == "ecl":
            if not is_real_eye_color(value):
                return False
        elif field == "pid":
            if not is_valid_pid(value):
                return False

    return True

def is_valid_hair_color(value):
    if len(value) != 7:
        return False

    try:
        num = int(value[1:], 16)
        return True
    except:
        return False
    
def year_within_range(value, min, max):
    if len(value) != 4:
        return False
            
    year = int(value)
    if year < min or year > max:
        return False

    return True

def is_real_eye_color(value):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in eye_colors

def num_in_range(value, min, max):
    try:
        num = int(value)
        if num < min or num > max:
            return False
        
        return True
    except:
        return False

def is_valid_height(value):
    units = value[len(value) - 2:]
    value = value[0:len(value) - 2]
    if units == "in":
        return num_in_range(value, 59, 76)
    elif units == "cm":
        return num_in_range(value, 150, 193)
    else:
        return False

def is_valid_pid(value):
    if len(value) != 9:
        return False
    
    value = value.lstrip("0")
    num = 0
    try:
        num = int(value)
    except:
        return False
    
    return True

num_valid = 0
for passport in passports:
    is_valid = is_valid_passport(passport)
    if is_valid:
        num_valid = num_valid + 1

print("part 1", num_valid)

num_valid = 0
for passport in passports:
    is_valid = is_valid_passport_v2(passport)
    if is_valid:
        num_valid = num_valid + 1

print("part 2", num_valid)