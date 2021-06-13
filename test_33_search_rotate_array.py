import unittest

"""
write down thoughts
minor revision to binary search
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right) // 2
            if nums[left] <= nums[mid]:  # left subarray is sorted, right subarray is NOT sorted
                if nums[left] <= target <= nums[mid]:  # target is in left subarray
                    right = mid
                else:  # target is in right subarray
                    left = mid+1 # target strictly larger than nums[mid]

            else:  # left subarray is NOT sorted, right subarray is sorted
                if nums[mid] <= target <= nums[right]:  # target is in right subarray
                    left = mid
                else:
                    right = mid-1
        if nums[left] == target:
            return left
        return -1


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    def test2(self):
        self.assertEqual(-1, Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
    def test3(self):
        self.assertEqual(-1, Solution().search([1], 0))




if __name__ == '__main__':
    unittest.main()
