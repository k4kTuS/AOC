lines = open('in.txt').read().splitlines()
lines = [line[::-1] for line in lines]

grand_total = 0

i = 0
problem_numbers = []
while i < len(lines[0]):
    number = "".join([line[i] for line in lines[:-1] if line[i] != ' '])
    if number != "":
        problem_numbers.append(number)
    sign = lines[-1][i]
    if sign != ' ':
        grand_total += eval(f"{sign}".join(problem_numbers))
        problem_numbers = []
    i += 1

print(grand_total)
