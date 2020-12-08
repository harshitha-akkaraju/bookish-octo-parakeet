filename = "input.txt"

data = {}
filehandle = open(filename, 'r')
while True:
    line = filehandle.readline()
    if not line:
        break
    line = line.strip()
    n = int(line, base=10)
    data[n] = True


# part 1
a = 1
b = 1
for key in data:
    diff = 2020 - key
    if abs(diff) in data:
        a = key
        b = abs(diff)
        break

print("part 1")
print(a, " + ", b, " = ", (a + b))
print("product: ", (a * b))
print()

# part 2
nums = []
sums = {}
for k in data:
    nums.append(k)

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if i != j:
            sums[nums[i] + nums[j]] = (i, j)

a = 1
b = 1
c = 1
for i in range(0, len(nums)):
    diff = 2020 - nums[i]
    if abs(diff) in sums:
        indices = sums[abs(diff)]
        if i != indices[0] and i != indices[1]:
            a = nums[indices[0]]
            b = nums[indices[1]]
            c = nums[i]

print("part 2")
print(a, " + ", b, " + ", c, " = ", (a + b + c))
print("product: ", (a * b * c))