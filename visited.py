def visited(edges, node1, node2):
    nedges, m = edges.shape

    for i in range(1, nedges + 1):
        if ((edges[i - 1, 0] == node1 and edges[i - 1, 1] == node2) or
            (edges[i - 1, 0] == node2 and edges[i - 1, 1] == node1)):
            return i

    return 0
