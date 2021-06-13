import unittest
import bisect

"""
write down thoughts
bucket sort because we need to find the consecutive positive numbers, so the complexity is not o(nlogn)

[3,4,-1,1]
sort to be [1,-1,3,4], requires O(n)
then another loop to determine which number != index+1
complexity is O(2*n) so O(n)
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        for i in range(len(nums)):
            while nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1] != nums[i]:

                # nums[i]<=len(nums) to avoid index out of bound
                # swap nums[i] to the corresponding place, for example 3 to [?, ?, 3, ?]
                tmp = nums[nums[i]-1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] # this does NOT work, for some reason!!!
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1 # no missing values, len+1


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(2, Solution().firstMissingPositive([3,4,-1,1]))
    def test2(self):
        self.assertEqual(3, Solution().firstMissingPositive([1,2]))

if __name__ == '__main__':
    unittest.main()
