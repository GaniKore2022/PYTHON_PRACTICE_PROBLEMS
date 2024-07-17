# def prims(graph):
#     
#     visited=[]
#     weights=[]
#     weights[start]=0
#     heapq.heappush(queue,(0,start))
#     while len(queue)!=0:
#         cur_weight, cur_node=heapq.heappop(queue)
#         if cur_node in visited:
#             continue
#         for weight,node in graph[cur_node]:
#             if node not in visited and weight<weight[node]:
#                 weights[node]=weight
#                 parents[node]=cur_node
#                 heapq.heappush(queue,(weight,node))
#             visited.add(cur_node)
#     print(weights)
# 
# graph={}
# prims(graph)


import heapq

def prim(graph):
    mst = []
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)

    edges = [(cost, start_vertex, next_vertex) for next_vertex, cost in graph[start_vertex]]
    heapq.heapify(edges)

    while edges:
        cost, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, cost))

            for next_vertex, next_cost in graph[dest]:
                if next_vertex not in visited:
                    heapq.heappush(edges, (next_cost, dest, next_vertex))

    return mst

# Example usage:
graph = {
    'A': [('B', 28), ('F', 10)],
    'B': [('A', 28), ('C', 16), ('G', 14)],
    'C': [('B', 16), ('D', 12)],
    'D': [('E', 22), ('C', 12), ('G', 18)],
    'E': [('G', 24), ('D', 22), ('F', 25)],
    'F': [('A', 10), ('E', 25)],
    'G': [('B', 14),('E', 24),('D', 18)]
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)