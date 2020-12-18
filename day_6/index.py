filename = "input.txt"

filehandle = open(filename, 'r')

responses = []
groups_responses = ""

while True:
    line = filehandle.readline()
    if not line:
        break
    
    line = line.strip()

    if line == "":
        responses.append(groups_responses)
        groups_responses = ""
    else:
        groups_responses = groups_responses + " | " + line

if groups_responses != "":
    responses.append(groups_responses)

# organized by group
responses = [r.strip(" |") for r in responses]

# count the number of questions anyone's answered yes to
total_number_of_yeses = 0

for g_r in responses:
    groups = g_r.split(" | ")
    unique = set({})
    for g in groups:
        answers = list(g)
        unique = unique.union(answers)
    
    total_number_of_yeses = total_number_of_yeses + len(unique)

print("Number of questions anyone has answered yes to", total_number_of_yeses)

# count the number of questions everyone answered yes to
number_of_yeses_from_everyone = 0

all_responses = "abcdefghijklmnopqrstuvwxyz"

for g_r in responses:
    groups = g_r.split(" | ")
    common = set(all_responses)
    for g in groups:
        answers = list(g)
        common = common.intersection(answers)
   
    number_of_yeses_from_everyone = number_of_yeses_from_everyone + len(common)

print("Number of questions everyone has answered yes to", number_of_yeses_from_everyone)