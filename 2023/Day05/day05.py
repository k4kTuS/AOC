mapping_steps = 7

def p1(seeds, maps):
    location = None
    for seed in seeds:
        x = seed
        for i in range(0, mapping_steps):
            keys = sorted(maps[i])
            for key in keys:
                val, len = maps[i][key]
                if x >= key and x < key + len:
                    x = val + x - key
                    break
        if not location or location > x:
            location = x
    print(location)

def p2(seeds, maps):
    for i in range(0, mapping_steps):
        seeds = make_ranges(seeds, maps[i])
    print(min(seeds, key=lambda x: x[0])[0])

def make_ranges(ranges, map):
    new_ranges = []
    for range_start, range_len in ranges:
        range_pos = range_start
        while range_pos < range_start + range_len:
            x = range_pos
            nearest_key = None
            found = False
            keys = sorted(map)
            for key in keys:
                val, len = map[key]
                if x >= key and x < key + len:
                    offset = x - key
                    x = val + offset
                    new_len = min(len - offset, range_start + range_len - range_pos)
                    new_ranges.append((x, new_len))
                    range_pos += new_len
                    found = True
                    break
                elif nearest_key is None and key > x:
                    nearest_key = key
            if not found:
                offset = nearest_key - x if nearest_key else range_len
                new_len = min(offset, range_start + range_len - range_pos)
                new_ranges.append((x, new_len))
                range_pos += new_len
    return new_ranges
                          

def parse_maps(lines):
    maps = {}
    idx = 0
    for line in lines:
        if not line:
            continue
        if line[0].isalpha():
            idx += 1
            continue
        dest, source, len = line.split()
        if idx not in maps:
            maps[idx] = {}
        maps[idx][int(source)] = (int(dest), int(len))
    return maps


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [x.rstrip() for x in file.readlines()]
        seeds = list(map(int, lines[0].split(':')[-1].split()))
        seed_ranges = [(seeds[i*2], seeds[i*2+1]) for i in range(0, len(seeds)//2)]
        maps = parse_maps(lines[3:])

        p1(seeds, maps)
        p2(seed_ranges, maps)
        