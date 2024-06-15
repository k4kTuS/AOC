from enum import Enum

WEST = (0, -1)
NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)

neighbours = {
        '|': [NORTH, SOUTH],
        '-': [WEST, EAST],
        'L': [NORTH, EAST],
        'J': [NORTH, WEST],
        '7': [WEST, SOUTH],
        'F': [SOUTH, EAST],
        '.': []
    }

def build_path(lines, fill_area):
    field = []
    s_x = None
    s_y = None

    for y, line in enumerate(lines):
        tiles = []
        x = 0
        for x, tile in enumerate(line.rstrip()):
            tiles.append(tile)
            if tile == 'S':
                s_x = x
                s_y = y
        field.append(tiles)
    
    # Determine S type
    visited = [[False for y in range(0, len(field[0]))] for i in range(0, len(field))]
    visited[s_y][s_x] = True
    s_neighbours, s_type = find_start(field, s_x, s_y)
    
    nodes = [(s_y+n[0], s_x+n[1], 1) for n in s_neighbours]
    length = 0
    while len(nodes) > 0:
        node = nodes.pop(0)
        if visited[node[0]][node[1]]:
            continue
        else:
            length = node[2]
            visited[node[0]][node[1]] = True
            for n in neighbours[field[node[0]][node[1]]]:
                ny = node[0]+n[0]
                nx = node[1]+n[1]
                if not visited[ny][nx]:
                    nodes.append((ny, nx, node[2]+1))
    print(length)

    walls = ["J", "L", "|"]
    field[s_y][s_x] = s_type
    in_cnt = 0
    for y, row in enumerate(field):
        for x in range(0, len(row)):
            if not visited[y][x]:
                cnt_l = 0
                cnt_r = 0
                for i in range(0, x):
                    if visited[y][i] and field[y][i] in walls:
                        cnt_l += 1       
                for i in range(x, len(row)):
                    if visited[y][i] and field[y][i] in walls:
                        cnt_r += 1
                if cnt_l % 2 and cnt_r % 2:
                    in_cnt += 1
                    field[y][x] = "O"
    print(in_cnt)

        
def find_start(field, x, y):
    s_neigh = []
    if (y > 0):
        if SOUTH in neighbours[field[y-1][x]]:
            s_neigh.append(NORTH)
    if (x > 0):
        if EAST in neighbours[field[y][x-1]]:
            s_neigh.append(WEST)
    if (y + 1 < len(field)):
        if NORTH in neighbours[field[y+1][x]]:
            s_neigh.append(SOUTH)
    if (x + 1 < len(field[0])):
        if WEST in neighbours[field[y][x+1]]:
            s_neigh.append(EAST)
    for k, v in neighbours.items():
        if v == s_neigh:
            return s_neigh, k
        

with open("input.txt") as file:
    lines = file.readlines()
    build_path(lines, True)