banks = open('in.txt').read().splitlines()

jolts = []
for bank in banks:
    batteries = list(bank)

    first_id = 0
    second_id = len(batteries) - 1
    for i in range(len(batteries) - 1):
        if batteries[i] > batteries[first_id]:
            first_id = i
    for i in range(first_id + 1, len(batteries)):
        if batteries[i] > batteries[second_id]:
            second_id = i
    jolts.append(int(f"{batteries[first_id]}{batteries[second_id]}"))
print(sum(jolts))
