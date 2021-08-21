import unittest

"""
write down thoughts
use three separate vars to store the set of the three largest values
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest = second = third = -2 ** 31 - 1
        for num in nums:
            if num > largest:
                third = second
                second = largest
                largest = num
            elif num > second and num != largest:
                third = second
                second = num
            elif num > third and num != second and num != largest:
                third = num
        if third >= -2 ** 31:
            return third
        else:
            return largest


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().thirdMax([3, 2, 1]))

    def test2(self):
        self.assertEqual(1, Solution().thirdMax([3, 2, 2, 1]))

    def test3(self):
        self.assertEqual(2, Solution().thirdMax([2, 1]))

    def test4(self):
        self.assertEqual(2, Solution().thirdMax([1, 2, 2, 5, 3, 5]))


if __name__ == '__main__':
    unittest.main()
