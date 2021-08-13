import unittest

"""
write down thoughts
easiest binary search
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    if num > 4:
        return -1
    if num < 4:
        return 1
    else:
        return 0


class Solution:
    @staticmethod
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            guessed = guess(mid)
            if guessed == 0:
                return mid
            if guessed == -1:
                high = mid - 1
            else:
                low = mid + 1
        return low


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().guessNumber(100))


if __name__ == '__main__':
    unittest.main()
