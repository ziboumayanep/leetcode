from typing import List


class Solution:
    @classmethod
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

    @classmethod
    def two_sum_one_pass(self, nums: List[int], target: int):
        track = {}
        for i in range(len(nums)):
            if (target - nums[i]) in track:
               return [track[target - nums[i]], i]
            track[nums[i]] = i




if __name__ == '__main__':
    print(Solution.two_sum_one_pass([1, 4, 3], 7))
