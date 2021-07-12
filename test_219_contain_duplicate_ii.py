import unittest

"""
write down thoughts
1. create a hashmap to store the index of last seen value
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i, num in enumerate(nums):
            # note: you should NOT use if not hashmap.get(), because 0 is considered falsy!!!
            index = hashmap.get(num)
            if index is None or i - index > k:
                hashmap[num] = i
            else:
                return True
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test2(self):
        self.assertEqual(False, Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()
