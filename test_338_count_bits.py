import unittest

"""
write down thoughts
bottom up DP
1. if i is even, countBits is the same as i//2, if i is odd, countBits is 1 more than i//2
for example,
i=1 (01), countBits = 1
i=2 (10), countBits = 1
i=3 (11), countBits = 1+1
i=4 (100), countBits = 1
i=5 (101), countBits = 1+1
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0 for _ in range(n + 1)]
        res[1] = 1
        for i in range(2, n + 1):
            res[i] = res[i // 2] if i % 2 == 0 else res[i // 2] + 1
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([0, 1, 1], Solution().countBits(2))

    def test2(self):
        self.assertEqual([0, 1, 1, 2, 1, 2], Solution().countBits(5))


if __name__ == '__main__':
    unittest.main()
