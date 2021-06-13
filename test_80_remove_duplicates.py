import unittest

"""
write down thoughts
have a pointer to scan through the list, when duplicate is found remove from list
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_cnt = 1
        prev = 0
        curr = 0
        while curr < len(nums):
            if curr > 0 and prev == nums[curr]:
                if dup_cnt >= 2: # already repeated 2 times
                    nums.pop(curr)  # curr is popped from list, no need to move to right
                else: # <2 repeat
                    dup_cnt += 1
                    curr += 1 # curr move to right
            else: # not repeat, move on to next char, reset dup_cnt
                prev = nums[curr]
                curr += 1
                dup_cnt = 1

        return len(nums)


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 1, 2, 2, 3]
        self.assertEqual(5, Solution().removeDuplicates(nums))
        self.assertEqual([1, 1, 2, 2, 3], nums)

    def test2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        self.assertEqual(7, Solution().removeDuplicates(nums))
        self.assertEqual([0, 0, 1, 1, 2, 3, 3], nums)


if __name__ == '__main__':
    unittest.main()
