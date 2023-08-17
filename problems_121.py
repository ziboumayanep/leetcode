#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
def max_profit(prices: List[int]) -> int:
    max = 0
    i = 0
    j = 1
    while True:
        if j >= len(prices):
            return max
        left = prices[i]
        right = prices[j]
        next_interval = right - left

        if next_interval <= 0:
            i = j
            j += 1
            continue

        if next_interval > max:
            max = next_interval
        j += 1

def test_max_profit():
    assert max_profit([1, 2]) == 1
    assert max_profit([1, 2, 3]) == 2
    assert max_profit([1, 2, 0, 3]) == 3
    assert max_profit([2, 1, 0, 3]) == 3
    assert max_profit([2]) == 0

