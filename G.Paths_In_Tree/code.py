import sys


sys.setrecursionlimit(10**7)


class Node:
    # feel free to change fields
    def __init__(self, weight, parent) -> None:
        self.weight = weight
        self.parent = parent
        self.children = []


def get_number_of_upgoing_paths(node: Node, x: int, cur_sum: int = 0, prefix_sums: dict = {0: 1}) -> int:
    count = 0
    cur_sum += node.weight
    count += prefix_sums.get(cur_sum - x, 0)
    prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
    for child in node.children:
        count += get_number_of_upgoing_paths(child, x, cur_sum, prefix_sums)
    prefix_sums[cur_sum] -= 1

    return count


def read_tree(tree_size: int) -> Node:
    nodes = []
    root = None
    for i in range(tree_size):
        p, w = map(int, input().split())
        nodes.append(Node(w, p))
        if p == -1:
            root = nodes[i]
    for i in range(tree_size):
        if nodes[i].parent != -1:
            nodes[nodes[i].parent].children.append(nodes[i])
    return root


n, x = map(int, input().split())
tree = read_tree(n)
print(get_number_of_upgoing_paths(tree, x))
