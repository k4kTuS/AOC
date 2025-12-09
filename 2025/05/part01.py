lines =  open('in.txt').read().splitlines()

ranges = []
ingredients = []

ings = False
for line in lines:
    if line == "":
        ings = True
        continue

    if not ings:
        ranges.append(tuple(map(int, line.split('-'))))
    else:
        ingredients.append(int(line))

ranges = sorted(ranges, key=lambda x: x[0])
ingredients = sorted(ingredients, reverse=True)

n_ingredients = 0
for ingredient in ingredients:
    for ind, r in enumerate(ranges):
        start, end = r
        if start <= ingredient <= end:
            n_ingredients += 1
            break

print(n_ingredients)