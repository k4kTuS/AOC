from enum import Enum

WEST = (0, -1)
NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)

routes = {
        '|': {NORTH:NORTH, SOUTH:SOUTH},
        '-': {WEST:WEST, EAST:EAST},
        'L': {SOUTH:EAST, WEST:NORTH},
        'J': {SOUTH:WEST, EAST:NORTH},
        '7': {NORTH:WEST, EAST:SOUTH},
        'F': {NORTH:EAST, WEST:SOUTH},
        '.': {}
    }

def p1(lines):
    field = list()
    s_x = None
    s_y = None
    y = 0
    for line in lines:
        tiles = list()
        x = 0
        for tile in line.rstrip():
            tiles.append(tile)
            if (tile == 'S'):
                s_x = x
                s_y = y
            x += 1
        y += 1
        field.append(tiles)
    
    # Determine S type
    y, x, dir = find_start(field, s_x, s_y)
    len = 1
    while True:
        if field[y][x] == 'S':
            break

        dir = routes[field[y][x]].get(dir)
        y += dir[0]
        x += dir[1]
        len += 1
    print(len//2)
        
def find_start(field, x, y):
    if (x > 0):
        res = routes[field[y][x+1]].get(EAST)
        if res:
            return y, x+1, EAST
    if (x + 1 < len(field)):
        res = routes[field[y][x-1]].get(WEST)
        if res:
            return y, x-1, WEST
    if (y > 0):
        res = routes[field[y-1][x]].get(NORTH)
        if res:
            return y-1, x, NORTH
    if (y + 1 < len(field)):
        res = routes[field[y+1][x]].get(SOUTH)
        if res:
            return y+1, x, SOUTH
        

if __name__ == "__main__":
    with open("Day10/input.txt") as file:
        lines = file.readlines()
        p1(lines)