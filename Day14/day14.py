with open("Day14/input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
data = [[x for x in line] for line in lines]

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        # print(y, x)
        if data[y][x] == 'O':
            c = y
            while c > 0 and data[c-1][x] == '.':
                data[c][x] = '.'
                data[c-1][x] = 'O' 
                c -= 1

weight = 0
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == 'O':
            weight += len(data) - y
print(weight)

