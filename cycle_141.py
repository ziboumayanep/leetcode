from typing import Optional

import tools


def has_cycle(head: Optional[tools.ListNode]) -> bool:
    if head is None:
        return False
    first = head
    second = head
    while True:
        first = first.next if first and first.next else None
        second = second.next.next if second and second.next and second.next.next else None

        if first is None and second is None:
            return False
        elif first != second:
            continue
        else:
            return True


def test_has_cycle():
    node1 = tools.ListNode(2)
    node0 = tools.ListNode(3)
    node1.next = node0
    node0.next = node1
    assert has_cycle(node0)


def test_has_cycle1():
    node0 = tools.ListNode(0)
    node1 = tools.ListNode(1)
    node0.next = node1
    assert has_cycle(node0) is False
