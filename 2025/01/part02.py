rotations = [(r[:1], int(r[1:])) for r in open('in.txt').read().splitlines()]

pos_zero_cnt = 0
dial_start = pos = last_pos = 50

for dir, steps in rotations:
    start = pos
    if dir == 'R':
        pos += steps
        pos_zero_cnt += pos // 100 - start // 100
    else:
        pos -= steps
        pos_zero_cnt += (start-1) // 100 - (pos-1) // 100

print(pos_zero_cnt)
