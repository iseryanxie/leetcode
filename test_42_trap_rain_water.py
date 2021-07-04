import unittest

"""
write down thoughts
Suppose Max_Left(i) is the maximum height to the left of position i,
water stored at each position = max(0, min(Max_Left(i),Max_Right(i)) - height(i))
Approach 1
scan the heights to find Max_Left (from left to right), need O(n) space,
scan to find Max_Right(from right to left), need O(n) space,
find water trapped with the formula.

Approach 2, improve the space to O(1). No need to prescan and store two arrays.
1. Max_Left (as of now), Max_Right (as of now) initialized as begin and end of height array
2. left, right = 0, len(height)-1
3. Now if Max_left<=Max_right, left ++, otherwise right--. 
Suppose Max_left<=Max_right, Note that the min(Max_Left(i),Max_Right(i)) is Max_left, because Max_left is smaller,
it does not matter how big Max_right is, the bottleneck is Max_left.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        trapped = 0
        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left]) # update the max_left of this current location
                trapped += max(0, max_left - height[left]) # calculate the trapped water for this current location
            else:
                right -= 1
                max_right = max(max_right, height[right])
                trapped += max(0, max_right - height[right])
        return trapped


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(6, Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test2(self):
        self.assertEqual(9, Solution().trap([4, 2, 0, 3, 2, 5]))


if __name__ == '__main__':
    unittest.main()
