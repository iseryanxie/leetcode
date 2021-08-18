import unittest

"""
write down thoughts
1. recursions
2. check if the node is a left leave: it is on the left of its parent node and it is a leaf node, no left and right 
children.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     def leftLeavesVal(root, arr):
    #         if root:
    #             if root.left and not root.left.left and not root.left.right:
    #                 arr.append(root.left.val)
    #
    #             leftLeavesVal(root.left, arr)
    #             leftLeavesVal(root.right, arr)
    #         return arr
    #
    #     arr = []
    #     arr = leftLeavesVal(root, arr)
    #
    #     return sum(arr)


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.maxVal = 0

        def traverse(node, level, direction='left'):

            if node == None:
                return

            if level > 0:
                if direction == 'left' and node.left == None and node.right == None:
                    self.maxVal += node.val

            traverse(node.left, level + 1, 'left')
            traverse(node.right, level + 1, 'right')

        traverse(root, 0)
        return self.maxVal


class TestSolution(unittest.TestCase):
    def test1(self):
        node9 = TreeNode(val=9)
        node15 = TreeNode(val=15)
        node7 = TreeNode(val=7)
        node20 = TreeNode(val=20, left=node15, right=node7)
        node3 = TreeNode(val=3, left=node9, right=node20)
        self.assertEqual(24, Solution().sumOfLeftLeaves(node3))


if __name__ == '__main__':
    unittest.main()
