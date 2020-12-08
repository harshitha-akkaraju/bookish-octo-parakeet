filename = "input.txt"

map = []

filehandle = open(filename, 'r')
while True:
    line = filehandle.readline()
    if not line:
        break
    
    line = line.strip()
    row = list(line)
    map.append(row)

def in_the_map(position):
    i = position[0]
    j = position[1]
    
    return (i >= 0 and i < len(map)) and (j >= 0 and j < len(map[i]))

# part 1: slope right 3, down 1 => 211
position = (0, 0)
num_trees = 0
while in_the_map(position):
    i = position[0]
    j = position[1]

    if map[i][j] == '#':
        num_trees = num_trees + 1

    if (j + 3) >= len(map[i]):
        temp = j + 3
        position = (i + 1, temp % len(map[i]))
    else:
        position = (i + 1, j + 3)

print("part 1")
print("number of trees: ", num_trees)
print()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = []
for slope in slopes:
    right = slope[0]
    down = slope[1]

    position = (0, 0)
    num_trees = 0

    while in_the_map(position):
        i = position[0]
        j = position[1]

        if map[i][j] == '#':
            num_trees = num_trees + 1

        if (j + right) >= len(map[i]):
            temp = j + right
            position = (i + down, temp % len(map[i]))
        else:
            position = (i + down, j + right)
    
    print("slope right", right, "down", down)
    print("number of trees: ", num_trees)

    counts.append(num_trees)

answer = 1
for num in counts:
    answer = answer * num

print("product", answer)

