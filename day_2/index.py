filename = "input.txt"

data = []
data_part2 = []

filehandle = open(filename, 'r')
while True:
    line = filehandle.readline()
    if not line:
        break
    line = line.strip()
    
    parts = line.split(":")

    constraints = parts[0].split(" ")
    occurence_counts = constraints[0].split("-")

    min_count = int(occurence_counts[0], base=10)
    max_count = int(occurence_counts[1], base=10)

    letter = constraints[1].strip()
    password = parts[1].strip()

    policy = {
        "letter": letter,
        "min_count": min_count,
        "max_count": max_count,
        "password": password
    }

    policy_2 = {
        "letter": letter,
        "position_1": min_count,
        "position_2": max_count,
        "password": password
    }

    data.append(policy)
    data_part2.append(policy_2)

def is_valid_password(policy):
    password = policy["password"]
    letter = policy["letter"]
    min_count = policy["min_count"]
    max_count = policy["max_count"]

    count = password.count(letter)
    return count >= min_count and count <= max_count

def is_valid_password_v2(policy):
    password = policy["password"]
    letter = policy["letter"]
    position_1 = policy["position_1"] - 1
    position_2 = policy["position_2"] - 1

    chars = list(password)

    return (chars[position_1] == letter and chars[position_2] != letter) or (chars[position_1] != letter and chars[position_2] == letter)

num_valid = 0
for policy in data:
    is_valid = is_valid_password(policy)
    if is_valid:
        num_valid = num_valid + 1


print("part 1: ")
print("number of valid passwords: ", num_valid)
print()

num_valid = 0
for policy in data_part2:
    is_valid = is_valid_password_v2(policy)
    if is_valid:
        num_valid = num_valid + 1

print("part 2: ")
print("number of valid passwords: ", num_valid)