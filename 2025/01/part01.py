rotations = [(r[:1], int(r[1:])) for r in open('in.txt').read().splitlines()]

pos_zero_cnt = 0
dial_start = pos = 50

for dir, steps in rotations:
    pos = (pos + steps if dir == 'R' else pos - steps) % 100
    if pos == 0: pos_zero_cnt+= 1
print(pos_zero_cnt)
