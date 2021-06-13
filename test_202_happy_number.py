import unittest
import bisect

"""
write down thoughts
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        :type nums: List[int]
        :rtype: int
        """
        def sqrt_sum(num: int) -> int:
            sum = 0
            while num>0:
                mod = num % 10
                sum += mod*mod
                num = num//10
            return sum

        seen = {}
        while sqrt_sum(n) not in seen:
            ss = sqrt_sum(n)
            if ss==1:
                return True
            else:
                seen[ss] = 1
            n = ss

        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isHappy(19))


if __name__ == '__main__':
    unittest.main()
