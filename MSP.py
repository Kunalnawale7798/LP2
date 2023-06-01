def prim_mst(graph):
    vertices = len(graph)
    mst = []
    visited = [False] * vertices
    visited[0] = True

    for _ in range(vertices - 1):
        min_edge = [None, None, float('inf')]
        for u in range(vertices):
            if visited[u]:
                for v in range(vertices):
                    if not visited[v] and graph[u][v] and graph[u][v] < min_edge[2]:
                        min_edge = [u, v, graph[u][v]]
        u, v, weight = min_edge
        mst.append((u, v, weight))
        visited[v] = True
    return mst
# Example graph represetation
graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 5, 8],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

# Running prims algorithm
minimum_spanning_tree = prim_mst(graph)

# printing the mst
print("Edges in the minimum spanning tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"{u} - {v} : {weight}")