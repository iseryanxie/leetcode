import unittest

"""
write down thoughts
binary search between 0 and num//2
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        low = 0
        high = num // 2
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(True, Solution().isPerfectSquare(4))
    # def test2(self):
    #     self.assertEqual(True, Solution().isPerfectSquare(9))
    # def test3(self):
    #     self.assertEqual(False, Solution().isPerfectSquare(7))
    def test4(self):
        self.assertEqual(True, Solution().isPerfectSquare(1))


if __name__ == '__main__':
    unittest.main()
