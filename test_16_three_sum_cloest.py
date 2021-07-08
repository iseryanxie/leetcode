import unittest

"""
write down thoughts
three pointers
1. sort list
2. enumerate pointer i,
3. move two pointers j,k, find the closest sum for each i
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) < 3:
            res = nums.sum()
        else:
            res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum < target:
                    j += 1
                else:
                    k -= 1
                if abs(tmp_sum - target) < abs(res - target):
                    res = tmp_sum
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().threeSumClosest([-1, 2, 1, -4], 1))


if __name__ == '__main__':
    unittest.main()
