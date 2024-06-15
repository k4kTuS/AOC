with open("sample.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
instructions = {}

l = 0
while l < len(lines):
    if lines[l] == "":
       l+=1
       break
    idx = lines[l].find('{')
    label = lines[l][:idx]
    vals = lines[l][idx+1:-1].split(',')
    last = vals[-1]
    rest = vals[:-1]
    
    label_vals = []
    for val in rest:
      delim_i = val.find(":")
      t = val[1:delim_i]
      eq = val[delim_i+1:]
      label_vals.append((val[0], t, eq))
    instructions[label] = {"i": label_vals, "l": last}
    l+=1

accepted = []
while l < len(lines):
    vals = lines[l][1:-1].split(',')
    vals = [val.split('=') for val in vals]
    vals = {x:y for x,y in vals}

    state = "in"
    s = ""
    while True:
        s += ">" + state
        if state == "A":
            for v in vals.values():
                accepted.append(int(v))
            break
        if state == "R":
            break
        rules = instructions[state]["i"]
        state = instructions[state]["l"]
        for i, rule, dest in rules:
            eq = vals[i] + rule
            if eval(eq):
                state = dest
                break
    l+=1
print(sum(accepted))