import unittest

"""
write down thoughts
1. approach 1
convert list to a set, for loop to find the num not in the set, time: O(n), space: O(n)
2. approach 2
bucket sort idea, place the result in the first half of the list (in place and result list does not count in 
space complexity). time: O(2n), space: O(1)
"""
from typing import List

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         num_set = set(nums)
#         res = []
#         for i in range(1,len(nums)+1):
#             if i not in num_set:
#                 res.append(i)
#         return res


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for num in nums:
            res[num-1] = num

        r = 0
        for i in range(1,n+1):
            if res[i-1] == 0:
                res[r] = i
                r += 1
        return res[:r]



class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([5,6], Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))


if __name__ == '__main__':
    unittest.main()
