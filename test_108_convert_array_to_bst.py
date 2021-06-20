import unittest

"""
write down thoughts
recursion
1. find point in the middle of the range
2. convert the middle point to treenode
3. recurse on left of the middle point, recurse on right of the middle point
"""
import math
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def convert_to_bst(nums, left, right):
            mid = math.floor((left + right) / 2)
            node = TreeNode(val=nums[mid])
            if left <= mid - 1:
                node.left = convert_to_bst(nums, left, mid - 1)
            if right >= mid + 1:
                node.right = convert_to_bst(nums, mid + 1, right)
            return node

        return convert_to_bst(nums, 0, len(nums) - 1)


class TestSolution(unittest.TestCase):
    def test1(self):
        bst = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
        self.assertEqual(0, bst.val)
        self.assertEqual(-10, bst.left.val)
        self.assertEqual(-3, bst.left.right.val)
        self.assertEqual(5, bst.right.val)
        self.assertEqual(9, bst.right.right.val)
    def test2(self):
        bst = Solution().sortedArrayToBST([3,5,8])
        self.assertEqual(5, bst.val)
        self.assertEqual(3, bst.left.val)
        self.assertEqual(8, bst.right.val)


if __name__ == '__main__':
    unittest.main()
