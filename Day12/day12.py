mem = {}

def combinations(springs, groups):
    if len(springs) == 0:
        return 1 if len(groups) == 0 else 0
    if len(groups) == 0:
        return 1 if "#" not in springs else 0

    if (springs, groups) in mem.keys():
        return mem[(springs, groups)]

    total_combs = 0
    if springs[0] == ".":
        combs = combinations(springs[1:], groups)
        mem[(springs[1:], groups)] = combs
        total_combs += combs
    if springs[0] == "#":
        if len(springs) >= groups[0] and "." not in springs[:groups[0]]:
            if len(springs) == groups[0] or springs[groups[0]] != "#":
                combs = combinations(springs[groups[0]+1:], groups[1:])
                mem[(springs[groups[0]+1:], groups[1:])] = combs
                total_combs += combs
    if springs[0] == "?":
        # Dot option
        combs = combinations(springs[1:], groups)
        mem[(springs[1:], groups)] = combs
        total_combs += combs
        # Hashtag option
        if len(springs) >= groups[0] and "." not in springs[:groups[0]]:
            if len(springs) == groups[0] or springs[groups[0]] != "#":
                combs = combinations(springs[groups[0]+1:], groups[1:])
                mem[(springs[groups[0]+1:], groups[1:])] = combs
                total_combs += combs
    
    return total_combs

res = 0
p2_res = 0
with open("Day12/input.txt") as file:
    lines = file.readlines()
    for line in lines:
        springs, groups = line.split()
        # List not hashable + mutable
        groups = tuple(int(x) for x in groups.split(','))
        res += combinations(springs, groups)
    for line in lines:
       springs, groups = line.split()
       springs = "?".join([springs]*5)
       groups = tuple(int(x) for x in groups.split(',')*5)
       p2_res += combinations(springs, groups)
print(res)
print(p2_res)