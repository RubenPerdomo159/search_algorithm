# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
gz = search.GPSProblem('G', 'Z'
                       , search.romania)
nd = search.GPSProblem('N', 'D'
                       , search.romania)
mf = search.GPSProblem('M', 'F'
                       , search.romania)

locations = [ab, oe, gz, nd, mf]

for loc in locations:
    print(f"From {loc.initial} to {loc.goal}:")
    print("  BFS:", search.breadth_first_graph_search(loc).path())
    print("    Path Cost:", search.breadth_first_graph_search(loc).path_cost)
    print("  DFS:", search.depth_first_graph_search(loc).path())
    print("    Path Cost:", search.depth_first_graph_search(loc).path_cost)
    print("------------------------------------------------------------")

# TODO:
# Añadir nodos visitados y nodos generados en cada búsqueda
# Añadir branch and bound search
# añadir subestimación+


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
