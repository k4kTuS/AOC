


with open("Day9/input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
data = [[int(x) for x in line.split()] for line in lines ]

# Part 1
preds = []
for history in data:
    last_vals = [history[-1]]
    while True:
        history =list(map(lambda x, y: x - y, history[1:], history[:-1]))
        last_vals.append(history[-1])
        if history.count(0) == len(history):
            preds.append(sum(last_vals))
            break
print(sum(preds))

# Part 2
preds = []
for history in data:
    first_vals = [history[0]]
    while True:
        history =list(map(lambda x, y: x - y, history[1:], history[:-1]))
        first_vals.append(history[0])
        if history.count(0) == len(history):
            pred = 0
            first_vals.reverse()
            for i in range(1, len(first_vals)):
                pred = first_vals[i] - pred
            preds.append(pred)
            break
print(sum(preds))
