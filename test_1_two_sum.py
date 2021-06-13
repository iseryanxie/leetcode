import unittest

"""
write down thoughts
first attempt: 
1. sort the list
2. two pointers till meet in the middle
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[target - nums[i]], i]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([0, 1], Solution().twoSum([2, 11, 15, 7], 13))


if __name__ == '__main__':
    unittest.main()
