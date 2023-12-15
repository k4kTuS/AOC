import copy
from itertools import product

def mirror_vertical(grid, smudge=False):
    full = len(grid[0][0])
    half = full//2
    for x in range(1, full):
        diffs = 0
        for f in grid:
            if x <= half:
                left_slice = f[0][:x]
                right_slice = f[0][x:x+x]
            else:
                left_slice = f[0][x-(full-x):x]
                right_slice = f[0][x:]
            right_slice = right_slice[::-1]
            for c in range(0, len(left_slice)):
                if left_slice[c] != right_slice[c]:
                    diffs += 1
        if diffs == (1 if smudge else 0):
            return x
    return 0

def mirror_horizontal(grid, smudge=False):
    full = len(grid)
    half = full//2
    for x in range(1, full):
        diffs = 0
        if x <= half:
            upper_slice = grid[:x]
            lower_slice = grid[x:x+x]
        else:
            upper_slice = grid[x-(full-x):x]
            lower_slice = grid[x:]
        lower_slice = lower_slice[::-1]

        for r in range(0, len(lower_slice)):
            for c in range(0, len(lower_slice[r][0])):
                if lower_slice[r][0][c] != upper_slice[r][0][c]:
                    diffs += 1
        if diffs == (1 if smudge else 0):
            return x
    return 0

with open("Day13/input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
data = [[x for x in line.split()] for line in lines]

calculations = 0
fields = []
field = []
for y, l in enumerate(data):
    if l == []:
        fields.append(field)
        field = []
    else:
        field.append(l)
fields.append(field)

for f in fields:
    res = mirror_vertical(f)
    if not res:
        res = mirror_horizontal(f)
        calculations += 100 * res
    else:
        calculations += res
print(calculations)

calculations = 0
for f in fields:
    res = mirror_vertical(f, True)
    if not res:
        res = mirror_horizontal(f, True)
        calculations += 100 * res
    else:
        calculations += res
print(calculations)