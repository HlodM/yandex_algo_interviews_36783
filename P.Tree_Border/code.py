from typing import List


def get_tree_border(nodes: List, root_id: int) -> List[int]:

    border = [root_id]
    to_visit = [node for node in nodes[root_id] if node != -1]

    while to_visit:
        childs = []
        for idx, node in enumerate(to_visit):
            if idx in (0, len(to_visit)-1) or sum(nodes[node]) == -2:
                border.append(node)
            childs.extend(child for child in nodes[node] if child != -1)
        to_visit = childs

    return border


with open('input.txt') as f:
    size, root_id = map(int, f.readline().split())
    nodes = [0 for _ in range(size)]
    for i in range(size):
        nodes[i] = tuple(map(int, f.readline().split()))

print(*get_tree_border(nodes, root_id))
