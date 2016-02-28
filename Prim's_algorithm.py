# Reza Asad
# Algorithm Class
# Feb 27th, 2016
######################### Algorithms ########################
from heapq import heappush, heappop, heapify
# This finds the minimum spanning tree of a graph using Prim's
# greedy algorithm.
def prims_mst(G):
    num_vertices = len(G)
    seen = set()
    # take a starting point.
    # The alorithm does not depend on this.
    source = G.iterkeys().next()
    seen.add(source)
    source_connection = list(G[source])
    edge_costs =  source_connection
    heapify(edge_costs)

    selected_edges = []
    total_cost = 0
    while len(seen) != num_vertices:
        # Add the next vertex
        next_edge = heappop(edge_costs)
        total_cost += next_edge[0]
        selected_edges.append(next_edge[1])
        added_vertex = next_edge[1][2]
        seen.add(added_vertex)

        # Maintain the edges_cost vertex addition
        for edge in G[added_vertex]:
            if edge[1][2] not in seen:
                heappush(edge_costs, edge)
    return selected_edges, total_cost
######################## Main ###############################
# Extract the edges
#data_file = open('edges.txt')
graph = {'a':{(2, 'a-b'),(5,'a-c')}, 'b':{(1,'b-c'), (3,'b-d'), (2,'b-a')}, 'c':{(10,'c-d'),(1,'c-b'),(5,'c-a')}, 'd':{(10,'d-c'),(3,'d-b')}}
print prims_mst(graph)