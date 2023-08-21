from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_node(l: List[int]) -> Optional[ListNode]:
    match l:
        case []:
            return None
        case [first, *rest]:
            node = ListNode(val=first)
            current_node = node
            for v in rest:
                current_node.next = ListNode(val=v)
                current_node = current_node.next
            return node


def node_to_list(n: ListNode) -> List[int]:
    result = []
    node = n
    while node:
        result.append(node.val)
        node = node.next
    return result
