from copy import deepcopy

def get_weight(grid):
    weight = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 'O':
                weight += len(grid) - y
    return weight

with open("input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
data = [[x for x in line] for line in lines]

# P1
p1_data = deepcopy(data)
for y in range(0, len(p1_data)):
    for x in range(0, len(p1_data[y])):
        if p1_data[y][x] == 'O':
            c = y
            while c > 0 and p1_data[c-1][x] == '.':
                p1_data[c][x] = '.'
                p1_data[c-1][x] = 'O' 
                c -= 1
print(get_weight(p1_data))

num_iters = 1000000000
cycle_end = 0
positions = [data]
while True:
    data = deepcopy(data)
    cycle_end +=1
    #North
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == 'O':
                c = y
                while c > 0 and data[c-1][x] == '.':
                    data[c][x] = '.'
                    data[c-1][x] = 'O' 
                    c -= 1
    #West
    for x in range(0, len(data[0])):
        for y in range(0, len(data)):
            if data[y][x] == 'O':
                c = x
                while c > 0 and data[y][c-1] == '.':
                    data[y][c] = '.'
                    data[y][c-1] = 'O' 
                    c -= 1
    #South
    for y in range(len(data)-1, -1, -1):
        for x in range(0, len(data[y])):
            if data[y][x] == 'O':
                c = y
                while c < len(data)-1 and data[c+1][x] == '.':
                    data[c][x] = '.'
                    data[c+1][x] = 'O' 
                    c += 1
    #East
    for x in range(len(data[0])-1, -1, -1):
        for y in range(0, len(data)):
            if data[y][x] == 'O':
                c = x
                while c < len(data[0])-1 and data[y][c+1] == '.':
                    data[y][c] = '.'
                    data[y][c+1] = 'O' 
                    c += 1 
    found = False
    for pos in positions:
        if pos == data:
            found = True
            break
    if found:
        break
    positions.append(data)

cycle_start = positions.index(data)
cycle_len = cycle_end - cycle_start
final_data = positions[(num_iters-cycle_start) % cycle_len + cycle_start]

print(get_weight(final_data))