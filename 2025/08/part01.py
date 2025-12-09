import numpy as np

points = [
    (int(x), int(y), int(z))
    for line in open("in.txt").read().splitlines()
    for x, y, z in [line.split(",")]
]

next_cluster_id = 0
point_clusters = [None for _ in range(len(points))]
solo_points = set({i for i in range(len(points))})
clusters_to_points = {0: set()}

def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

distance_matrix = np.array([
    [euclidean_distance(p1, p2) if p1 != p2 else np.inf for p2 in points] for p1 in points
])

for i in range(1000): # Stop after N shortest connections
    arg_x, arg_y = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)
    distance_matrix[arg_x][arg_y] = np.inf
    distance_matrix[arg_y][arg_x] = np.inf

    if point_clusters[arg_x] is None and point_clusters[arg_y] is None:
        # print(f"Creating new cluster {next_cluster_id} with points {arg_x} ({points[arg_x]}) and {arg_y} ({points[arg_y]})")
        clusters_to_points[next_cluster_id] = set([arg_x, arg_y])

        point_clusters[arg_x] = next_cluster_id
        point_clusters[arg_y] = next_cluster_id
        
        next_cluster_id += 1
        solo_points.remove(arg_x)
        solo_points.remove(arg_y)

    elif point_clusters[arg_x] is None and point_clusters[arg_y] is not None:
        # print(f"Adding point {arg_x} ({points[arg_x]}) to cluster {point_clusters[arg_y]} based on point {arg_y} ({points[arg_y]})")
        clusters_to_points[point_clusters[arg_y]].add(arg_x)

        point_clusters[arg_x] = point_clusters[arg_y]
        solo_points.remove(arg_x)

    elif point_clusters[arg_x] is not None and point_clusters[arg_y] is None:
        # print(f"Adding point {arg_y} ({points[arg_y]}) to cluster {point_clusters[arg_x]} based on point {arg_x} ({points[arg_x]})")
        clusters_to_points[point_clusters[arg_x]].add(arg_y)

        point_clusters[arg_y] = point_clusters[arg_x]
        solo_points.remove(arg_y)

    elif point_clusters[arg_x] != point_clusters[arg_y]: # Joining two clusters
        # print(f"Merging clusters {point_clusters[arg_x]} and {point_clusters[arg_y]} into {point_clusters[arg_x]} based on points {arg_x} ({points[arg_x]}) and {arg_y} ({points[arg_y]})")
        new_main_cluster = point_clusters[arg_x]
        old_removed_cluster = point_clusters[arg_y]
        
        for point in clusters_to_points[old_removed_cluster]:
            point_clusters[point] = new_main_cluster
            clusters_to_points[new_main_cluster].add(point)
        del clusters_to_points[old_removed_cluster]

    # else:
        # print(f"Points {arg_x} ({points[arg_x]}) and {arg_y} ({points[arg_y]}) are already in the same cluster {point_clusters[arg_x]} - {point_clusters[arg_y]}")

    # print(point_clusters)
    # print('---'*20)

# for cluster, points in sorted(clusters_to_points.items(), key= lambda x: len(x[1])):
#     print(f"Cluster {cluster} with {len(points)} points")

top_3_clusters = sorted(clusters_to_points.items(), key= lambda x: len(x[1]), reverse=True)[:3]
lengths = []

for cluster, points in top_3_clusters:
    print(f"Cluster {cluster} with {len(points)} points")
    lengths.append(len(points))

import math
print("Result:", math.prod(lengths))