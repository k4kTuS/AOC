import heapq

def find_path(grid, ultra=False):
    neighbours = [(0,1), (1,0), (0,-1), (-1,0)]
    states = set()
    q = [(0,0,0,0,0,0)]
    while q:
        cost, pos_y, pos_x, m_y, m_x, steps = heapq.heappop(q)
        if pos_y == len(grid)-1 and pos_x == len(grid[-1])-1:
            return(cost)
        if (pos_y, pos_x, m_y, m_x, steps) in states:
            continue
        states.add((pos_y, pos_x, m_y, m_x, steps))

        m = (m_y, m_x)
        rev_turn = (-m_y, -m_x)

        for n in neighbours:
            if not ultra:
                if n == rev_turn or (n == m and steps == 3):
                    continue
            else:
                if n == rev_turn or (n == m and steps == 10) or (n != m and steps < 4 and m != (0,0)):
                    continue

            n_y = pos_y + n[0]
            n_x = pos_x + n[1]
            n_steps = 1 if n != m else steps + 1

            if n_y < 0 or n_x < 0 or n_y == len(grid) or n_x == len(grid[n_y]):
                continue
            heapq.heappush(q, (cost+grid[n_y][n_x],n_y, n_x,n[0],n[1],n_steps))

with open("input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
    grid = [list(map(int, line)) for line in lines]
    
    print(find_path(grid, False)) #p1
    print(find_path(grid, True)) #p2


