move = {"L": (0,-1), "R": (0,1), "U": (-1,0), "D": (1,0)}
move_p2 = {"2": (0,-1), "0": (0,1), "3": (-1,0), "1": (1,0)}

with open("input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
    
    pos = (0,0)
    perim=0
    vertices = []
    pos_p2 = (0,0)
    perim_p2 = 0
    vertices_p2 = []
    for line in lines:
        direction, steps, c = line.split()
        steps = int(steps)
        pos = (pos[0] + move[direction][0]*steps, pos[1] + move[direction][1]*steps)
        vertices.append(pos)
        perim += steps

        dir_p2 = c[-2]
        steps_p2 = int(c[2:-2], 16)
        pos_p2 = (pos_p2[0] + move_p2[dir_p2][0]*steps_p2, pos_p2[1] + move_p2[dir_p2][1]*steps_p2)
        vertices_p2.append(pos_p2)
        perim_p2 += steps_p2

    #p1    
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][1] * vertices[j][0]
        area -= vertices[j][1] * vertices[i][0]
    # Inside area using Triangle formula (shoelace)
    area = abs(area)//2
    # Calculate on-points using Pick's theorem
    inside = area - perim//2 + 1
    print(inside + perim)

    #p2
    n = len(vertices_p2)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices_p2[i][1] * vertices_p2[j][0]
        area -= vertices_p2[j][1] * vertices_p2[i][0]
    # Inside area using Triangle formula (shoelace)
    area = abs(area)//2
    # Calculate on-points using Pick's theorem
    inside = area - perim_p2//2 + 1
    print(inside + perim_p2)