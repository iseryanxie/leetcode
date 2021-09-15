import unittest

"""
write down thoughts
check 1..sqrt(num), rule out sqrt(num) and itself.
"""
from typing import List


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        i = 1
        sum = 0
        while i * i <= num:
            if num % i == 0:
                sum += i
                if i * i != num:
                    sum += num // i
            i += 1
        return num == sum - num


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().checkPerfectNumber(28))


if __name__ == '__main__':
    unittest.main()
