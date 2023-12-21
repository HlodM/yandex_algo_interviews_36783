from node import Node


# Comment it before submitting
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.neighbours = []


def cloneGraph(node) -> Node:
    clones = {node.val: Node(node.val)}
    stack = [node]
    while stack:
        cur_node = stack.pop()
        clone_node = clones[cur_node.val]
        for neigh in cur_node.neighbours:
            if neigh.val not in clones:
                clones[neigh.val] = Node(neigh.val)
                stack.append(neigh)
            clone_node.neighbours.append(clones[neigh.val])

    return clones[node.val]
