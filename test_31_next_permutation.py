import unittest

"""
write down thoughts
1. from right to left, if keep increasing, you find largest number, just reverse the list
2. when you find a decreased number, say n, now try to find the number to the right of this n that is just larger than n,
say m, now swap n with m
3. then reverse the numbers to the right of the new m, you will get the next permutation.
For example,
[1,5,4,2]
1. method 1
start from 2->4->5, all increasing, now 5->1, 1 is "n". now we find the number in [5,4,2] that is just larger than 1, 
which is 2. [1,5,4,2] is the largest number start with 1, so swap 1 with 2 (that is just larger than 1). we get [2,5,4,1]
we know that [5,4,1] is in the decreasing order, and the next permutation is just the reverse [1,4,5], so the next 
permutation is [2,1,4,5].
2. method 2
From right to left, find i where the first number that is smaller than the number to the right, in this case 1. 
Now reverse everything to the right of i. [1,2,4,5]. Now starting from [2,4,5], from left to right, find the 
first number that is greater than 1, in this case 2. Now swap 2 and 1, you got [2,1,4,5]
Both are the same. But Method 2 is easier to implement.
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            nums[i],nums[j] = nums[j], nums[i]
        def reverse(nums,i,j):
            for k in range(i,(i+j)//2+1):
                swap(nums,k,i+j-k)
        n = len(nums)
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:
            i -= 1
        reverse(nums,i,n-1)
        # reverse to the right of i-1, takes care of both cases of all increasing (i=0) or not all increasing, need to reverse
        if i>0: # need to swap if i>0
            for j in range(i,n):
                if nums[j]>nums[i-1]: # i-1 is the number that is greater than i.
                    swap(nums,i-1,j)
                    break # must break, only swap i-1 and j, do not continue



class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1,2,3]
        Solution().nextPermutation(nums)
        self.assertEqual([1, 3, 2], nums)
    def test2(self):
        nums = [3,2,1]
        Solution().nextPermutation(nums)
        self.assertEqual([1, 2, 3], nums)
    def test3(self):
        nums = [4,3,1,2]
        Solution().nextPermutation(nums)
        self.assertEqual([4,3,2,1], nums)
    def test4(self):
        nums = [1]
        Solution().nextPermutation(nums)
        self.assertEqual([1], nums)


if __name__ == '__main__':
    unittest.main()
