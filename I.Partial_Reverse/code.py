from node import Node


# Comment it before submitting
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


def Reverse(head: Node, left: int, right: int) -> Node:
    if left == right:
        return head
    dummy = Node(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    current = prev.next

    for _ in range(right - left):
        next_node = current.next
        current.next, next_node.next, prev.next = next_node.next, prev.next, next_node

    return dummy.next
