import unittest

"""
write down thoughts
"""
from typing import List

class Solution(object):
    def template(self, arr, key) -> int:
        return 4


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().template([1, 2, 3, 4, 5], 5))


if __name__ == '__main__':
    unittest.main()
