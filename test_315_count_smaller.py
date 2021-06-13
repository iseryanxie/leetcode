import unittest

"""
write down thoughts
1. from right to left of the list
2. return bisect.bisect_left index, which represents how many numbers in the processed numbers are smaller than this number
3. add to result
4. add number to processed list (this is now ordered ascending)
5. when all numbers are finished, return result[::-1], because we need left to right 
"""
import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 从左往右处理，右边是未知的，所以不好弄
        # 从右往左处理，则对于每个数，其右边的数都已知
        processed_num = []
        res = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(processed_num,
                                     num)  # bisect to return the index of where num sits in processed_num list
            res.append(idx)
            processed_num.insert(idx, num)
        return res[::-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 1, 1, 0], Solution().countSmaller([5, 2, 6, 1]))

    def test2(self):
        self.assertEqual([0, 0], Solution().countSmaller([-1, -1]))

    def test3(self):
        self.assertEqual([3, 1, 2, 1, 0], Solution().countSmaller([5, 2, 6, 2, 1]))


if __name__ == '__main__':
    unittest.main()
