with open("input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
res = 0
for instruction in lines[0].split(','):
    i_hash = 0
    for c in instruction:
        i_hash += ord(c)
        i_hash *= 17
        i_hash = i_hash % 256
    res += i_hash
print(res)


boxes = [[] for x in range(256)]
lenses = {}
for instruction in lines[0].split(','):
    label_hash = 0
    label = ""
    focal_lens = -1
    for i, c in enumerate(instruction):
        if c not in ['=', '-']:
            label += c
            label_hash += ord(c)
            label_hash *= 17
            label_hash = label_hash % 256
        else:
            if c == '=':
                focal_lens = int(instruction[-1])
                break
            elif c == '-':
                break
    if focal_lens == -1:
        if label in boxes[label_hash]:
            boxes[label_hash].remove(label)
            lenses[label] = -1
    else:
        lenses[label] = focal_lens
        if label not in boxes[label_hash]:
            boxes[label_hash].append(label)

hashmap_res = 0
for i, box in enumerate(boxes):
    for z, instruction in enumerate(box):
        hashmap_res += (i+1)*(z+1)*lenses[instruction]
print(hashmap_res)