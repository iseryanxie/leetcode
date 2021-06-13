import unittest
import bisect

"""
write down thoughts
use bisect to keep an ordered array
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        return (self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]) / 2 if len(self.nums) % 2 == 0 else \
        self.nums[len(self.nums) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class TestSolution(unittest.TestCase):
    def test1(self):
        obj = MedianFinder()
        obj.addNum(1)
        obj.addNum(2)

        self.assertEqual(1.5, obj.findMedian())
        obj.addNum(3)
        self.assertEqual(2, obj.findMedian())


if __name__ == '__main__':
    unittest.main()
