import unittest
import bisect

"""
write down thoughts
Approach 1
count, then populate x*0+y*1+z*2
Approach 2
1. create three pointers: left, middle, right
2. if middle == 0, swap it with left, left++, 
3. if middle == 1, move on
4. if middle == 2, swap it with right
high level 
nums[0..left]==0
nums[left+1..middle-1]==1
nums[middle]=?
nums[right..end]==2
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1 # left and right represent the boundary of the colors
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1 # region 0 has one more element
                i += 1 # we are swapping with a 1, except when there is no 1 yet then we are swapping 0s,
                # so i no need to check again, i++
            elif nums[i] == 1:
                i += 1 # nums[i] is 1, keep it in the region 0, move to next element
            else:
                nums[i], nums[right] = nums[right], nums[i] # we don't know the value of nums[right], so no change i
                right -= 1


class TestSolution(unittest.TestCase):
    def test1(self):
        colors = [2, 0, 2, 1, 1, 0]
        Solution().sortColors(colors)
        self.assertEqual([0, 0, 1, 1, 2, 2], colors)


if __name__ == '__main__':
    unittest.main()
