import unittest
import bisect

"""
write down thoughts
"""


class Solution(object):
    def binary_search(self, arr, start, end, key):
        if end >= start:
            mid = (start + end) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return self.binary_search(arr, start, mid - 1, key)
            else:
                return self.binary_search(arr, mid + 1, end, key)
        else:
            return -1

    def template(self, arr, key) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        while arr[r] < key:
            r = r * 2
        if r > len(arr) - 1:
            r = len(arr) - 1
        print(r)
        return self.binary_search(arr, 0, r, key)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(10046, Solution().template([i for i in range(100000)], 10046))


if __name__ == '__main__':
    unittest.main()
