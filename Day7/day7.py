def make_standings(hands, comp_fn):
    standings = sorted(hands, key = lambda x: (comp_fn(x['cards']), x['cards']))
    res = 0
    
    for i, hand in enumerate(standings):
        res += (i+1) * hand['bid']
    print(res)

def get_combo(hand):
    count_dict = {c: hand.count(c) for c in hand}
    counts = list(count_dict.values())
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        return 4 if 2 in counts else 3
    if 2 in counts:
        return 2 if counts.count(2) > 1 else 1
    else:
        return 0

def get_combo_joker(hand):
    j_cnt = hand.count('0')
    if j_cnt == 0:
        return get_combo(hand)

    count_dict = {c: hand.count(c) for c in hand if c !='0'}
    counts = sorted(list(count_dict.values()))

    if j_cnt >= 4:
        return 6
    if j_cnt == 3:
        return 6 if counts == [2] else 5
    if j_cnt == 2:
        if counts == [3]:
            return 6
        if counts == [1, 2]:
            return 5
        if counts == [1, 1, 1]:
            return 3
    if j_cnt == 1:
        if counts == [4]:
            return 6
        if counts == [1, 3]:
            return 5
        if counts == [2, 2]:
            return 4
        if counts == [1, 1, 2]:
            return 3
        if counts == [1, 1, 1, 1]:
            return 1

if __name__ == "__main__":
    with open("Day7/input.txt") as file:
        lines = [x.rstrip() for x in file.readlines()]
    vals = [x.split() for x in lines]
    cards = [x[0].translate(str.maketrans("TJQKA", "ABCDE")) for x in vals]
    bids = [int(x[1]) for x in vals]
    hands = [{'cards': cards[i],'bid': bids[i]} for i in range(0, len(vals))]
    make_standings(hands, get_combo)
    
    cards_j = [x.replace('B', '0') for x in cards]
    hands = [{'cards': cards_j[i],'bid': bids[i]} for i in range(0, len(vals))]
    make_standings(hands, get_combo_joker)


     