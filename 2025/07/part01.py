grid = [list(line) for line in open('in.txt').read().splitlines()]

# Find S
positions = set()
splits = 0
for i, c in enumerate(grid[0]):
    if c == 'S':
        positions.add(i)
        break

for _, line in enumerate(grid):
    new_positions = set()
    remove = set()

    for position in positions:
        if line[position] == '^':
            new_positions.add(position-1)
            new_positions.add(position+1)
            remove.add(position)
            splits += 1
    positions = positions.union(new_positions).difference(remove)

print(splits)
