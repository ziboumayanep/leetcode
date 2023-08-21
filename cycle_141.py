from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    first = head
    second = head
    while True:
        next_first = first.next if first.next else None
        next_second = second.next.next if second.next and second.next.next else None
        if next_first is None and next_second is None:
            return False
        elif next_first != next_second:
            continue
        else:
            return True

def test_has_cycle():
    pass

