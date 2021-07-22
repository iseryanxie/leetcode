import unittest

"""
write down thoughts
binary search, then find the left most and right most of the number equals to target
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, findleft):
            left = 0
            right = len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    res = mid
                    if findleft:
                        right = mid - 1
                    else:
                        left = mid + 1
            return res

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        return [left, right]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([3, 4], Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

    def test2(self):
        self.assertEqual([2, 4], Solution().searchRange([5, 7, 8, 8, 8, 10], 8))

    def test3(self):
        self.assertEqual([-1, -1], Solution().searchRange([5, 7, 8, 8, 8, 10], 9))

    def test4(self):
        self.assertEqual([-1, -1], Solution().searchRange([], 0))


if __name__ == '__main__':
    unittest.main()
