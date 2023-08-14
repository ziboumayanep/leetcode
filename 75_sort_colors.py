from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        track = {}
        for n, i in enumerate(nums):
            if n == 0:
                continue

