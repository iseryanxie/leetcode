import unittest

"""
write down thoughts
"""
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(area ** 0.5)
        for i in range(w, 0, -1):
            if area % i == 0:
                return [area // i, i]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 2], Solution().constructRectangle(4))


if __name__ == '__main__':
    unittest.main()
