import re

def p1(lines):
    numbers = []
    for l, line in enumerate(lines):
        found = False
        number = ""
        for i, c in enumerate(line):
            if c.isdigit():
                number = number + c
                if not found:
                    for move in [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]:
                        if l + move[0] < 0 or l + move[0] > len(lines) - 1 or i + move[1] < 0 or i + move[1] > len(line) - 1:
                            continue
                        symbol = lines[l + move[0]][i + move[1]]
                        if not symbol.isdigit() and symbol != '.':
                            found = True
                            break
            else:
                if found:
                    found = False
                    numbers.append(int(number))
                number = ""
        if found:
            numbers.append(int(number))
    print(sum(numbers))

def p2(lines):
    gears = {}
    for l, line in enumerate(lines):
        found = False
        number = ""
        gear_cords = []
        for i, c in enumerate(line):
            if c.isdigit():
                number = number + c
                if not found:
                    for move in [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]:
                        move_l = l + move[0]
                        move_i = i + move[1]
                        if move_l < 0 or move_l > len(lines) - 1 or move_i < 0 or move_i > len(line) - 1:
                            continue
                        symbol = lines[move_l][move_i]
                        if symbol == '*':
                            found = True
                            gear_cords.append((move_l, move_i))
                            break
            else:
                if found:
                    found = False
                    for gear in gear_cords:
                        if gear in gears:
                            gears[gear].append(int(number))
                        else:
                            gears[gear] = [int(number)]
                gear_cords = []
                number = ""
        if found:
            for cords in gear_cords:
                if cords in gears:
                    gears[cords].append(int(number))
                else:
                    gears[cords] = [int(number)]
    res = 0
    for nums in gears.values():
        if len(nums) == 2:
            res = res + nums[0] * nums[1]
    print(res)

if __name__ == "__main__":
    with open("Day3/input.txt") as file:
        lines = [x.rstrip() for x in file.readlines()]
        p1(lines)
        p2(lines)