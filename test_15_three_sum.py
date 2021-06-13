import unittest

"""
write down thoughts
1. sort list
2. for each number from 0 to len(nums)-2(not inclusive), dedup by skipping the number that is the same as previous
3. two pointer to check (dedup)
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        res = []
        for i,a in enumerate(nums):
            if i == 0 or (i > 0 and nums[i] > nums[i - 1]):  # skip duplicate num
                left, right = i + 1, l - 1
                while left < right:
                    tmps=a + nums[left] + nums[right]
                    if  tmps== 0:
                        res.append([a, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif tmps>0:
                        right -= 1
                    elif tmps<0:
                        left += 1
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum([-1, 0, 1, 2, -1, -4]))

    def test2(self):
        self.assertEqual([], Solution().threeSum([]))

    def test3(self):
        self.assertEqual([], Solution().threeSum([0]))


if __name__ == '__main__':
    unittest.main()
