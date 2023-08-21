from typing import Optional, List

from tools import ListNode, create_list_node, node_to_list


def reversed_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    current = head
    next_node = current.next
    node_before = None
    while next_node is not None:
        temp_node = next_node.next
        current.next = node_before
        node_before = current
        current = next_node
        next_node = temp_node
        if next_node is None:
            current.next = node_before
    return current


def test_reversed_list():
    node = create_list_node([1, 2, 3, 4, 5])
    reversed = reversed_list(node)
    result = node_to_list(reversed)
    assert result == [5, 4, 3, 2, 1]
