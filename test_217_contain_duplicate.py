import unittest

"""
write down thoughts
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value_set = set()
        for value in nums:
            if value in value_set:
                return True
            else:
                value_set.add(value)
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().containsDuplicate([1,2,3,1]))


if __name__ == '__main__':
    unittest.main()
