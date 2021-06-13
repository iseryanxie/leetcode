import unittest

"""
write down thoughts
1. handle special k and points
2. sort points using custom compare methods
3. return first k
"""


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not points or k == 0:
            return []
        if k >= len(points):
            return points
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]


class TestSolution(unittest.TestCase):
    def test1(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        self.assertEqual(Solution().kClosest(points, k), [[3, 3], [-2, 4]])

    def test2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 0
        self.assertEqual(Solution().kClosest(points, k), [])

    def test3(self):
        points = []
        k = 1
        self.assertEqual(Solution().kClosest(points, k), [])

    def test4(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 10
        self.assertEqual(Solution().kClosest(points, k), [[3, 3], [5, -1], [-2, 4]])

    def test5(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        self.assertEqual(Solution().kClosest(points, k), [[-2, 2]])


if __name__ == '__main__':
    unittest.main()
