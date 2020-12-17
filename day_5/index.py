import sys

filename = "input.txt"

boarding_passes = []

filehandle = open(filename, 'r')
while True:
    line = filehandle.readline()
    if not line:
        break
    
    line = line.strip()
    boarding_passes.append(line)

def search(low, high, letter, min_letter):
    if letter == min_letter:
        new_high = int((low + high) / 2)
        return (low, new_high)
    
    new_low = int((low + high) / 2) + 1
    return (new_low, high)

max_seat_id = -sys.maxsize - 1
seat_ids = []

for b in boarding_passes:
    rows = b[0:len(b) - 3]
    cols = b[len(b) - 3:]

    row_low = 0
    row_high = 127

    for char in rows:
        new_range = search(row_low, row_high, char, 'F')
        row_low = new_range[0]
        row_high = new_range[1]
    
    col_low = 0
    col_high = 7

    for char in cols:
        new_range = search(col_low, col_high, char, 'L')
        col_low = new_range[0]
        col_high = new_range[1]
    
    row = row_low
    col = col_low
    seat_id = (row * 8) + col

    max_seat_id = max(max_seat_id, seat_id)

    seat_ids.append(seat_id)

print("max seat id:", max_seat_id)

seat_ids.sort()

# missing seat id
my_seat_id = 0
for index in range (0, len(seat_ids) - 1):
    c = seat_ids[index]
    n = seat_ids[index + 1]

    if n != (c + 1):
        my_seat_id = c + 1
        break

print("my seat id: ", my_seat_id)
