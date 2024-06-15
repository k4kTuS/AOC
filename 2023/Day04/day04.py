def p1(lines):
    points = 0
    for line in lines:
        card_points = 0
        w, e = line.split(':')[-1].split('|')
        w_nums = w.split()
        e_nums = e.split()
        
        for w_num in w_nums:
            for e_num in e_nums:
                if w_num == e_num:
                    card_points = 1 if card_points == 0 else card_points * 2
                    break
        points += card_points
    print(points)

def p2(lines):
    card_counts = [1 for x in range(0, len(lines))]
    for l, line in enumerate(lines):
        w_count = 0
        w, e = line.split(':')[-1].split('|')
        w_nums = w.split()
        e_nums = e.split()
        
        for w_num in w_nums:
            for e_num in e_nums:
                if w_num == e_num:
                    w_count += 1
                    break
        for i in range(1, w_count+1):
            card_counts[l+i] += card_counts[l]
    print(sum(card_counts))

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [x.rstrip() for x in file.readlines()]
        p1(lines)
        p2(lines)