lines = open('in.txt').read().splitlines()
lines = [" ".join(line.split()) for line in lines]
lines = [line.split() for line in lines]

grand_total = 0

for problem in range(len(lines[0])):
    sign = lines[-1][problem]
    numbers = [line[problem] for line in lines[:-1]]
    grand_total += eval(f"{sign}".join(numbers))
print(grand_total)