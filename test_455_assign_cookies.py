import unittest

"""
write down thoughts
sort greed factor and cookie size
starting from largest to smallest, assign largest cookie to greediest kid, if satisfied, count, otherwise, 
move to next greediest kis, till all kids are assigned or running out of cookie.
"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        count = 0
        for i in range(n-1,-1,-1):
            if len(s)!= 0 and g[i]<=s[-1]:  # greediest kid g[i] is satisfied by s[-1],
                # otherwise g[i] cannot be satisfied at all, skip to the next g[i-1]
                count += 1
                s.pop()
        return count


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().findContentChildren([1, 2, 3], [1, 1]))


if __name__ == '__main__':
    unittest.main()
