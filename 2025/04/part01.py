lines = open('in.txt').read().splitlines()

moves = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

rows = len(lines)
cols = len(lines[0])

paper_cnt = 0
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
            paper_cnt += 1

print(paper_cnt)

