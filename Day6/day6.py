def p1(times, distances):
    wins = []
    for z in range(0, len(times)):
        win_ops = 0
        for t in range(0, times[z]):
            if t * (times[z] - t) > distances[z]:
                win_ops += 1
        wins.append(win_ops)
    res = 1
    for w in wins:
        res *= w
    print(res)

def p2(time, distance):
    idx = None
    lo = 0
    hi = time // 2
    
    if hi * (time - hi) <= distance:
        print(0)
        return

    while lo <= hi:
        mid = (lo + hi) // 2
        if (mid * (time - mid)) <= distance:
            lo = mid+1
        else:
            idx = mid
            hi = mid-1
    print(int((time/2-idx)*2+1))

if __name__ == "__main__":
    with open("Day6/input.txt") as file:
        lines = [x.rstrip() for x in file.readlines()]
        times = list(map(int, lines[0].split(':')[-1].split()))
        distances = list(map(int, lines[1].split(':')[-1].split()))
        p1(times, distances)

        time = int(lines[0].split(':')[-1].replace(" ", ""))
        distance = int(lines[1].split(':')[-1].replace(" ", ""))
        p2(time, distance)

        