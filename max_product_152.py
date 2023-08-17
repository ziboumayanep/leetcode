from typing import List


def max_product(nums: List[int]) -> int:
    max_until_here = 1
    max_result = max(nums)
    min_until_here = 1
    for i in nums:
        if i == 0:
            _max = 1
            _min = 1
        else:
            _max = max_until_here * i
            _min = min_until_here * i
        max_until_here = max(_max, _min, i)
        min_until_here = min(_max, _min, i)
        if i == 0:
            max_result = max(0, max_result)
        else:
            max_result = max(max_result, max_until_here)

    return max_result


def test_max_product():
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([2, 3, 0, -2, 4]) == 6
    assert max_product([-2]) == -2
    assert max_product([3, -1, 4]) == 4
    assert max_product([-3, 0, 1, -2]) == 1
    assert max_product([2,-5,-2,-4,3]) == 24
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-1, -1, 0]) == 1
