banks = open('in.txt').read().splitlines()

jolts = []
n_batteries = 12

for bank in banks:
    indexes = []
    last_index = 0
    selected_index = 0
    for bat in range(1, n_batteries + 1):
        for i in range(last_index + 1, len(bank) - n_batteries + bat):
            if bank[i] > bank[selected_index]:
                selected_index = i
            last_index = selected_index
        indexes.append(selected_index)
        selected_index += 1
    jolts.append((
        indexes,
        int(''.join([bank[idx] for idx in indexes])),
        bank
    ))


def highlight_indices(s, indices, color="\033[91m"):
    reset = "\033[0m"
    result = ""

    for i, ch in enumerate(s):
        if i in indices:
            result += f"{color}{ch}{reset}"
        else:
            result += ch

    return result

for i, v, b in jolts:
    print('-'*100)
    print(highlight_indices(b, i))
    print(v, f"({len(b)})", ':', i)

print(sum([v for _, v, _ in jolts]))