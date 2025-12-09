values = open('in.txt').read().split(',')
values = [tuple(map(int, val.split('-'))) for val in values]

invalid_ids = []

for start_id, end_id in values:
    for num in range(start_id, end_id+1, 1):
        val = str(num)
        if len(val) % 2 != 0:
            continue
        middle_idx = len(val) // 2
        if val[:middle_idx] == val[middle_idx:]:
            invalid_ids.append(int(val))
print(sum(invalid_ids))
print(invalid_ids)