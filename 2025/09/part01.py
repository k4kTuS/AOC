import numpy as np

points = [
    (int(x), int(y))
    for line in open("in.txt").read().splitlines()
    for x, y in [line.split(",")]
]

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

distance_matrix = np.array([
    [manhattan_distance(p1, p2) if p1 != p2 else -np.inf for p2 in points] for p1 in points
])

arg_x, arg_y = np.unravel_index(np.argmax(distance_matrix), distance_matrix.shape)
p1 = points[arg_x]
p2 = points[arg_y]
print("Points:", p1, p2)

area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
print("Area:", area)