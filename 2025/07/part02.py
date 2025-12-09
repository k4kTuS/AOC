grid = [list(line) for line in open('in.txt').read().splitlines()]

# Prepare counts of paths that lead to each position
grid_entries = [
    [0 for _ in range(len(grid[0]))]
    for _ in range(len(grid))
]
positions = set()
# Find S
for i, c in enumerate(grid[0]):
    if c == 'S':
        grid_entries[0][i] = 1
        positions.add(i)
        break

for row in range(1, len(grid)):
    new_positions = set()
    remove = set()

    for position in positions:
        # Beam splits
        if grid[row][position] == '^':
            # Prepare positions after split
            new_positions.add(position-1)
            new_positions.add(position+1)
            remove.add(position)
            # Increase the count of paths that lead to the new positions
            grid_entries[row][position-1] += grid_entries[row-1][position]
            grid_entries[row][position+1] += grid_entries[row-1][position]
        else:
            # Increase the count of paths that lead to the new positions 
            grid_entries[row][position] += grid_entries[row-1][position]
    # Update active positions in the new row
    positions = positions.union(new_positions).difference(remove)

print(sum(grid_entries[-1]))