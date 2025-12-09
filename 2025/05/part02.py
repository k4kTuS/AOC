lines =  open('in.txt').read().splitlines()

ranges = []
ingredients = []

for line in lines:
    if line == "":
        break
    ranges.append(tuple(map(int, line.split('-'))))

ranges = sorted(ranges, key=lambda x: (x[0], x[1]))

current_range_id = 0
clean_ranges = [ranges[0]]

for r in ranges[1:]:
    curr_start, curr_end = clean_ranges[current_range_id]
    r_start, r_end = r

    if r_start > curr_end:
        clean_ranges.append((r_start, r_end))
        current_range_id += 1
        continue

    if r_end > curr_end:
        clean_ranges[current_range_id] = (curr_start, r_end)

n_ids = 0
for start,end in clean_ranges:
    n_ids += end - start + 1
print(n_ids)
