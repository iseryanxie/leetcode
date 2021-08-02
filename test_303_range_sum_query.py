import unittest

"""
write down thoughts
1. keep the cumsum of the whole list
2. add an extra 0 to the left of the cumsum
"""

from typing import List
class NumArray:

    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     self.cumsum = {0:0}
    #
    #     for i in range(1,len(nums)):
    #
    #         self.cumsum[i] = self.cumsum[i-1] +nums[i]
    #
    # def sumRange(self, left: int, right: int) -> int:
    #     return self.cumsum[right]-self.cumsum[left]+self.nums[left]
    def __init__(self, nums: List[int]):
        cumsum = 0
        self.cumsum = []
        self.cumsum.append(cumsum)
        for i in range(len(nums)):
            cumsum += nums[i]
            self.cumsum.append(cumsum)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right + 1] - self.cumsum[left]


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, nums.sumRange(0,2))


if __name__ == '__main__':
    unittest.main()
