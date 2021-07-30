import unittest

"""
write down thoughts
= binary search
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version == 1:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left<right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left

class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(4, Solution().firstBadVersion(5))
    def test2(self):
        self.assertEqual(1, Solution().firstBadVersion(1))



if __name__ == '__main__':
    unittest.main()
