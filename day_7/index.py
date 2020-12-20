filename = "input.txt"

def extract_colors(line):
    colors = []

    parts = line.split(" contain ")
    parts[0] = parts[0].strip()
    parent_color = parts[0][0:len(parts[0]) - 4]
    colors.append(parent_color.strip())

    parts[1] = parts[1].strip()
    child_bags = parts[1].split(", ")
    for child_bag in child_bags:
        if child_bag != "no other bags.":
            chunks = child_bag.split(" ")
            color = chunks[1] + " " + chunks[2]
            colors.append(color.strip())
    
    return colors


def construct_matrix(rules, color_index):
    length = len(color_index.keys())
    matrix = [[0] * length for i in range (length)]

    for rule in rules:
        parts = rule.split(" contain ")

        parent_bag = parts[0][0:len(parts[0])-4]
        parent_bag = parent_bag.strip()
        parent_bag_index = color_index[parent_bag]

        child_bags = parts[1].split(",")
        child_bags = [c.strip() for c in child_bags]

        for child_bag in child_bags:
            if child_bag != "no other bags.":
                chunks = child_bag.split(" ")
                quantity = int(chunks[0], 10)
                color = chunks[1] + " " + chunks[2]

                child_bag_index = color_index[color]

                matrix[parent_bag_index][child_bag_index] = quantity
    
    return matrix

# depth first search
def traverse(start, matrix, color_index):
    stack = []
    stack.append(start)
    seen = {}

    while len(stack) != 0:
        node = stack.pop()
        if node not in seen:
            seen[node] = True
            child_nodes = get_child_nodes(node, matrix)
            for c in child_nodes:
                stack.append(c)
    
    return color_index["shiny gold"] != start and color_index["shiny gold"] in seen

def get_child_nodes(node, matrix):
    children = matrix[node]

    child_nodes = []
    for i in range (0, len(children)):
        if children[i] != 0:
            child_nodes.append(i)
    return child_nodes

def extend(complete, partial):
    for p in partial:
        if p not in complete:
            complete.append(p)
    
    return complete

def main():
    filehandle = open(filename, 'r')

    rules = []
    color_index = {}
    colors = []

    # read input file
    while True:
        line = filehandle.readline()
        if not line:
            break
        
        line = line.strip()

        temp_colors = set(extract_colors(line))
        colors = extend(colors, temp_colors)

        rules.append(line)
    
    # create color index
    for i in range (0, len(colors)):
        color_index[colors[i]] = i
    
    matrix = construct_matrix(rules, color_index)

    # find the number of bags to contain at least 1 shiny golden bag
    number_of_bags = 0
    for i in range(0, len(colors)):
        seen = traverse(i, matrix, color_index)
        if seen:
            number_of_bags = number_of_bags + 1

    print("number of bags to contain at least 1 shiny golden bag", number_of_bags)

if __name__ == "__main__":
    main()