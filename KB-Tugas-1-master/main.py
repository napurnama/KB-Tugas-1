from node import Node
from dependencies import *

#SOLUTIONS IN 3, 11, 31, 45, 47, 49, 63, 307
goal = [0,1,2,3,4,5,6,7,8]
state = [3,1,2,4,7,5,6,0,8]

gen_amt = 12
test_node = Node(goal, state)

# uncomment one
dfs(test_node, gen_amt)
# bfs(test_node)
# mismatched_tiles_solution(test_node)
# manhattan_distance_solution(test_node)
# simple_hill_climb(test_node)

print(f"""{test_node.amt} node(s) expanded.""")