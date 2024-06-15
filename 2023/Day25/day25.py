import networkx as nx

with open("input.txt") as file:
    lines = [x.rstrip() for x in file.readlines()]
    g = nx.Graph()

    for line in lines:
        v, right = line.split(':')
        for v2 in right.split():
            g.add_edge(v, v2)
            g.add_edge(v2, v)
    # Should probably check if there are 3 edges
    edges = nx.minimum_edge_cut(g)
    g.remove_edges_from(edges)
    l,r = nx.connected_components(g)
    print(len(l)*len(r))
