import unittest

"""
write down thoughts
You can win if n is Not a multiple of 4, because you can take 1-3 to make sure there is 4*k left for your opponent. 
When there is 4 left, whoever needs to take now, will lose, because he/she can only take 1-3 now.
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().canWinNim(1))


if __name__ == '__main__':
    unittest.main()
