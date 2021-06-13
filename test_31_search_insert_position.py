import unittest

"""
write down thoughts
binary search template
"""
from typing import List

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if len(nums)==0:
#             return 0
#         left, right = 0, len(nums)-1
#         if target>nums[right]:
#             return right+1
#         if target<=nums[left]:
#             return 0
#         while left<right:
#             mid = (left+right)//2
#             if nums[mid] == target:
#                 return mid
#             if nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid-1
#
#         return left if nums[left]==target else left+1 if nums[left]<target else left-1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)

        while (l + 1 < r):
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid

        return r

class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(2, Solution().searchInsert([1, 3,5,6], 5))
    # def test2(self):
    #     self.assertEqual(1, Solution().searchInsert([1, 3,5,6], 2))
    # def test3(self):
    #     self.assertEqual(4, Solution().searchInsert([1, 3,5,6], 7))
    # def test4(self):
    #     self.assertEqual(0, Solution().searchInsert([1, 3,5,6], 0))
    # def test5(self):
    #     self.assertEqual(0, Solution().searchInsert([1], 0))
    # def test6(self):
    #     self.assertEqual(0, Solution().searchInsert([1], 1))
    def test7(self):
        self.assertEqual(2, Solution().searchInsert([1,3,5], 4))





if __name__ == '__main__':
    unittest.main()
