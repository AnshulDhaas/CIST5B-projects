def num_edges(edges):
    edge_map = {}
    num = 0

    for u, v in edges:
        if u == v:
            num += 1
            continue

        edge_key = (u, v) if u < v else (v, u)
        if edge_key in edge_map:
            num += 1
        
        edge_map[edge_key] = edge_map.get(edge_key, 0) + 1

    return num

adj_list = [ (5, 10), (10, 20), (5, 10), (20, 25), (10, 30), (30, 5), (20, 25), (5, 10), (10, 10) ]

print(num_edges(adj_list))