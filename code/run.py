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
    
    result_bfs = search.breadth_first_graph_search(loc)
    print("  BFS:", result_bfs.path())
    print("    Path Cost:", result_bfs.path_cost)
    print("    Generated Nodes:", loc.generated)
    print("    Visited Nodes:", loc.visited)
    print()

    loc.generated = 0
    loc.visited = 0
    result_dfs = search.depth_first_graph_search(loc)
    print("  DFS:", result_dfs.path())
    print("    Path Cost:", result_dfs.path_cost)
    print("    Generated Nodes:", loc.generated)
    print("    Visited Nodes:", loc.visited)
    print()

    loc.generated = 0
    loc.visited = 0
    result_bb = search.branch_and_bound(loc)
    print("  Branch and Bound:", result_bb.path())
    print("    Path Cost:", result_bb.path_cost)
    print("    Generated Nodes:", loc.generated)
    print("    Visited Nodes:", loc.visited)
    print()

    loc.generated = 0
    loc.visited = 0
    result_bb_h = search.branch_and_bound(loc, use_estimation=True)
    print("  Branch and Bound with estimation:", result_bb_h.path())
    print("    Path Cost:", result_bb_h.path_cost)
    print("    Generated Nodes:", loc.generated)
    print("    Visited Nodes:", loc.visited)
    print("------------------------------------------------------------")



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
