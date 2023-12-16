def valid(move, grid):
    return 0 <= move[0] and move[0] < len(grid)\
        and 0 <= move[1] and move[1] < len(grid[move[0]])

def energize(pos, grid):
    energized = [[{
        "e": False,
        (0, 1): False,
        (0, -1): False,
        (1, 0): False,
        (-1, 0): False
    } for i in range(len(grid[z]))] for z in range(len(grid))]

    nodes = []
    nodes.append(pos)
    while len(nodes) > 0:
        pos_y, pos_x, mov_y, mov_x = nodes.pop(0)
        field = grid[pos_y][pos_x]
        
        if energized[pos_y][pos_x][(mov_y, mov_x)]:
            continue
        else:
            energized[pos_y][pos_x]['e'] = True
            energized[pos_y][pos_x][(mov_y, mov_x)] = True

        moves = []
        if field == '.':
            moves.append((pos_y+mov_y, pos_x+mov_x, mov_y, mov_x))
        elif field == '|':
            if mov_y == -1:
                moves.append((pos_y-1, pos_x, -1, 0))
            elif mov_y == 1:
                moves.append((pos_y+1, pos_x, 1, 0))
            else:
                moves.append((pos_y-1, pos_x, -1, 0))
                moves.append((pos_y+1, pos_x, 1, 0))
        elif field == '-':
            if mov_x == -1:
                moves.append((pos_y, pos_x-1, 0, -1))
            elif mov_x == 1:
                moves.append((pos_y, pos_x+1, 0, 1))
            else:
                moves.append((pos_y, pos_x-1, 0, -1))
                moves.append((pos_y, pos_x+1, 0, 1))
        elif field == "\\":
            if mov_y == -1:
                moves.append((pos_y, pos_x-1, 0, -1))
            elif mov_y == 1:
                moves.append((pos_y, pos_x+1, 0, 1))
            elif mov_x == -1:
                moves.append((pos_y-1, pos_x, -1, 0))
            elif mov_x == 1:
                moves.append((pos_y+1, pos_x, 1, 0))
        elif field == "/":
            if mov_y == -1:
                moves.append((pos_y, pos_x+1, 0, 1))
            elif mov_y == 1:
                moves.append((pos_y, pos_x-1, 0, -1))
            elif mov_x == -1:
                moves.append((pos_y+1, pos_x, 1, 0))
            elif mov_x == 1:
                moves.append((pos_y-1, pos_x, -1, 0))
        for move in moves:
                if valid(move, grid):
                    nodes.append(move)

    cnt = 0
    for row in energized:
        for c in row:
            if c['e']:
                cnt += 1
    return cnt

with open("Day16/input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
grid = [[c for c in line] for line in lines]

print(energize((0,0,0,1), grid))

results = []
for y in range(len(grid)):
    results.append(energize((y, 0, 0, 1), grid))
    results.append(energize((y, len(grid[y])-1, 0, -1), grid))
for x in range(len(grid[0])):
    results.append(energize((0, x, 1, 0), grid))
    results.append(energize((len(grid)-1, x, 1, 0), grid))

print(max(results))


