import sys

values = open('in.txt').read().split(',')
values = [tuple(map(int, val.split('-'))) for val in values]

invalid_ids = []

def divisors(n):
    return [i for i in range(1, n) if n % i == 0]

for start_id, end_id in values:
    for num in range(start_id, end_id+1, 1):
        val = str(num)
        divs = divisors(len(val))
        for div in divs:
            vals = [val[div*i : div*(i+1)] for i in range(len(val)//div)]
            if len(set(vals)) == 1:
                invalid_ids.append(num)
                break
print(sum(invalid_ids))
# print(invalid_ids)
