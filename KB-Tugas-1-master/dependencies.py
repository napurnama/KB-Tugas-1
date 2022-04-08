def printFromLeaf(leaf):
    if bool(leaf.parent):
        printFromLeaf(leaf.parent)
    leaf.toString()


def dfs(root, gen, dfsFound=[False]):
    # print(goalFound)
    if root.isGoal():
        dfsFound[0] = True
        print("=================\n=================\n")
        print(f"DFS FOUND SOLUTION IN THE {root.gen}-TH GENERATION (STEP) WITH {root.amt} NODES EXPANDED")
        print("\n=================\n=================")
        printFromLeaf(root)
    if dfsFound[0]:
        pass
    if not root.isGoal() and bool(gen):
        root.reproduce()
        for child in root.children:
            dfs(child, gen-1, dfsFound=dfsFound)


def bfs(root, qiu=[], bfsFound=[False]):
    if root.isGoal(): 
        bfsFound[0] = True
        print("=================\n=================\n")
        print(f"BFS FOUND SOLUTION IN THE {root.gen}-TH GENERATION (STEP) WITH {root.amt} NODES EXPANDED")
        print("\n=================\n=================")
        printFromLeaf(root)
    elif bfsFound[0]: 
        pass
    else: 
        root.reproduce()
        for child in root.children:
            qiu.append(child)
        if len(qiu): 
            temp = qiu.pop(0)
            bfs(temp, qiu=qiu, bfsFound=bfsFound)
        else: #root not goal && bfs has not found && qiu is empty
            print(f"{root.isGoal()} and {bfsFound[0]} and {len(qiu)}")
            print("=================\n=================\n")
            print(f"BFS COULD NOT FIND SOLUTION WITHIN TREE")
            print("\n=================\n=================")


def mismatched_tiles_solution(root, qiu=[], goalFound=[False]):
    if root.isGoal():
        goalFound[0] = True
        print("=================\n=================\n")
        print(f"MISMATCHED TILE SOLUTION IN THE {root.gen}-TH GENERATION (STEP) WITH {root.amt} NODES EXPANDED")
        print("\n=================\n=================")
        printFromLeaf(root)
    elif goalFound[0]:
        pass
    else:
        root.reproduce()
        for child in root.children:
            if bool(len(qiu)):
                for i in range(len(qiu)):
                    if qiu[i].h1 + qiu[i].gen > child.h1 + child.gen:
                        qiu.insert(i, child)
                    if i >= len(qiu) - 1 and qiu[i].h1 + qiu[i].gen <= child.h1 + child.gen:
                        qiu.append(child)
                pass
            else:
                qiu.append(child)
        if bool(len(qiu)):
            temp = qiu.pop(0)
            mismatched_tiles_solution(temp, qiu=qiu, goalFound=goalFound)
        else:
            print("=================\n=================\n")
            print(f"NO MISMATCHED TILE SOLUTION FOUND")
            print("\n=================\n=================")


def manhattan_distance_solution(root, qiu=[], goalFound=[False]):
    if root.isGoal():
        goalFound[0] = True
        print("=================\n=================\n")
        print(f"MANHATTAN SOLUTION IN THE {root.gen}-TH GENERATION (STEP) WITH {root.amt} NODES EXPANDED")
        print("\n=================\n=================")
        printFromLeaf(root)
    elif goalFound[0]:
        pass
    else:
        root.reproduce()
        for child in root.children:
            if bool(len(qiu)):
                for i in range(len(qiu)):
                    if qiu[i].h2 + qiu[i].gen > child.h2 + child.gen:
                        qiu.insert(i, child)
                    if i >= len(qiu) - 1 and qiu[i].h2 + qiu[i].gen <= child.h2 + child.gen:
                        qiu.append(child)
                pass
            else:
                qiu.append(child)
        if bool(len(qiu)):
            temp = qiu.pop(0)
            manhattan_distance_solution(temp, qiu=qiu, goalFound=goalFound)
        else:
            print("=================\n=================\n")
            print(f"NO MANHATTAN SOLUTION FOUND")
            print("\n=================\n=================")


def simple_hill_climb(node):
    while not node.isGoal():
        flag = 0
        node.reproduce()
        for child in node.children:
            if child.h1 < node.h1:
                node = child
                flag = 1
                break
        if flag == 0:
            break

    if node.isGoal():
        print("=================\n=================\n")
        print(f"HILL CLIMB SOLUTION IN THE {node.gen}-TH GENERATION (STEP) WITH {node.amt} NODES EXPANDED")
        print("\n=================\n=================")

        printFromLeaf(node)

    else:
        print("=================\n=================\n")
        print(f"NO HILL CLIMB SOLUTION FOUND")
        print("\n=================\n=================")
        

    return node