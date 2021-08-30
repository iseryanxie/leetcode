import unittest

"""
write down thoughts
use xor(^) to find the difference in bits
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y  # use xor operation to find the difference
        # convert to bit and count
        count = 0
        while x:
            if x & 1 == 1:
                count += 1
            x >>= 1  # shift bit
        return count


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().hammingDistance(1, 4))


if __name__ == '__main__':
    unittest.main()
