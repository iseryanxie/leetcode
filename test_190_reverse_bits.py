import unittest

"""
write down thoughts
1. Use template of digit reversal, the difference is this is base 10, while LC 7 is base 2.
2. Use << and >> to shift digit. 
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            digit = n%2
            ans = ans*2+digit
            n = n//2
            # ans = (ans << 1) | (n & 1)
            # n >>= 1
        return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(964176192, Solution().reverseBits(43261596))


if __name__ == '__main__':
    unittest.main()
