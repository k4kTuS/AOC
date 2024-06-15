def distances(galaxies, scale):
    distances = []
    for i, gal1 in enumerate(galaxies):
        y1 = gal1[0] + gal1[2]*scale
        x1 = gal1[1] + gal1[3]*scale

        for gal2 in galaxies[i+1:]:
            y2 = gal2[0] + gal2[2]*scale
            x2 = gal2[1] + gal2[3]*scale
            if scale > 1:
                distances.append(abs((y1 - gal1[2]) - (y2 - gal2[2]))+abs((x1 - gal1[3]) - (x2 - gal2[3])))
            else:
                distances.append(abs(y1 - y2)+abs(x1 - x2))
    print(sum(distances))

def p2():
    pass

if __name__ == "__main__":
    with open("input.txt") as file:
        galaxies = []
        offset = 0
        lines = [x.rstrip() for x in file.readlines()]
        for y, line in enumerate(lines):
            has_gal = False
            for x, char in enumerate(line):
                if char == '#':
                    galaxies.append([y,x, offset, 0])
                    has_gal = True
            if not has_gal:
                offset += 1

        col_idxs = []
        for x in range(0, len(lines[0])):
            has_gal = False
            for galaxy in galaxies:
                if galaxy[1] == x:
                    has_gal = True
                    break
            if not has_gal:
                col_idxs.append(x)
            
        for galaxy in galaxies:
            cnt = 0
            for idx in col_idxs:
                if galaxy[1] > idx:
                    cnt += 1
            galaxy[3] += cnt

        distances(galaxies, 1) #p1
        distances(galaxies, 1000000) #p2

        