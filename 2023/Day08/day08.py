import math

def find_simple_path(graph, directions):
    node = "AAA"
    steps = 0
    dir_id = 0
    while node != "ZZZ":
        node = graph[node][directions[dir_id]]
        dir_id = (dir_id + 1) % len(directions)
        steps += 1
    print(steps)

def find_all_paths(graph, start_nodes, directions):
    steps = [0 for i in range(0, len(start_nodes))]
    for i, node in enumerate(start_nodes):
        dir_id = 0
        while not node.endswith('Z'):
            node = graph[node][directions[dir_id]]
            dir_id = (dir_id + 1) % len(directions)
            steps[i] += 1
    print(math.lcm(*steps))


with open("input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
directions = [c for c in lines[0]]

graph = {}
start_nodes = []
for line in lines[2:]:
    vals = line.split()
    node = vals[0]
    left = vals[2][1:-1]
    right = vals[3][0:-1]
    graph[node] = {'L': left, 'R': right}
    if node.endswith('A'):
        start_nodes.append(node)

find_simple_path(graph, directions)
find_all_paths(graph, start_nodes, directions)
    

     