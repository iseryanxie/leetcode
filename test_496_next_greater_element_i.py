import unittest

"""
write down thoughts
1. bruteforce solution, two for loop to find the first greater number
2. for loop in nums2 to find the next greater number to the right of each element, then store such mapping to a hashmap
use each element nums1 to generate the result by searching in the hashmap
"""
from typing import List


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for num1 in nums1:
#             start = False
#             found = False
#             for num2 in nums2:
#                 if num1 == num2:
#                     start = True
#                 if start and num2 > num1:
#                     res.append(num2)
#                     found = True
#                     break
#             if not found:
#                 res.append(-1)
#         return res

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        for i in range(len(nums2)):
            found = False
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    next_greater[nums2[i]] = nums2[j]
                    found = True
                    break
            if not found:
                next_greater[nums2[i]]= -1
        return [next_greater[n] for n in nums1]

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([-1, 3, -1], Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    def test2(self):
        self.assertEqual([3, -1], Solution().nextGreaterElement([2,4], [1,2,3,4]))


if __name__ == '__main__':
    unittest.main()
