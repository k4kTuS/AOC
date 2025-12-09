lines = open('in.txt').read().splitlines()
lines = [list(l) for l in lines]

moves = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

rows = len(lines)
cols = len(lines[0])

paper_cnt = 0
while True:
    positions = []
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != '@':
                continue
            cnt = 0
            for r_move, c_move in moves:
                r_ind = r + r_move
                c_ind = c + c_move

                if 0 <= r_ind < rows and 0 <= c_ind < cols:
                    if lines[r_ind][c_ind] == '@':
                        cnt += 1
            if cnt < 4:
                positions.append((r, c))
                paper_cnt += 1
    if len(positions) == 0:
        break
    for r_ind, c_ind in positions:
        lines[r_ind][c_ind] = 'x'

print(paper_cnt)

