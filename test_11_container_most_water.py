import unittest

"""
write down thoughts
1. Brute Force (time limit exceeded) O(n^2)
left, right pointer, res = max (res, (r-l)*min(height(r),height(l))), left++, ...
2. Two Pointers O(n)
left, right pointer, start from the beginning and end of the list, work towards the middle.
move the pointer of left or right whoever is smaller, then keep track of the maximum area.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max = 0
        while left < right:
            hl = height[left]
            hr = height[right]
            area = (right - left) * min(hl, hr)
            if area > max:
                max = area
            if hl <= hr:
                left += 1
            else:
                right -= 1
        return max


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(49, Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    unittest.main()
