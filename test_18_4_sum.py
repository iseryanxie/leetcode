import unittest

"""
write down thoughts
- write a general kSum function
1. recursive call kSum() with k-1
2. kSum(k=2) will call twoSum, which uses a two-pointer method
3. remove duplicates and handle easy case
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums: List[int], target: int):
            """assume sorted"""
            res = []
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target or (l > 0 and nums[l] == nums[l - 1]): # skip duplicates
                    l += 1
                elif nums[l] + nums[r] > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res

        def kSum(nums: List[int], target: int, k: int):
            """assume sorted"""
            res = []
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target: # skip obvious cases
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]: # skip duplicates
                    for _, kset in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + kset)
            return res

        nums.sort()

        return kSum(nums, target, 4)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], Solution().fourSum([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    unittest.main()
