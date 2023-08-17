from typing import List, Tuple, Optional


def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    i = 0
    j = len(nums) - 1
    while i < j:
        left = nums[i]
        right = nums[j]
        sum = left + right
        if sum == target:
            return i, j
        elif sum > target:
            j -= 1
            continue
        else:
            i += 1
            continue
    return None

def test_two_sum_sorted():
    assert two_sum_sorted([1, 2, 3], 4) == (0, 2)
    assert two_sum_sorted([-1, 1, 2, 3], 4) == (1, 3)
    assert two_sum_sorted([-1, 1, 2, 3], 0) == (0, 1)
