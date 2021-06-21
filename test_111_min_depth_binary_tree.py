import unittest

"""
write down thoughts
recursion
note that only leaf node counts, therefore, you can't just use what's in 102, because it will return 0 for a subtree 
without left branch. minor revision to handle that case.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1  # leaf node
        if root.left is None:  # if no left leaf, but there is a right leaf, it does not count as leaf node
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


class TestSolution(unittest.TestCase):
    def test1(self):
        node15 = TreeNode(val=15)
        node7 = TreeNode(val=7)
        node20 = TreeNode(val=20, left=node15, right=node7)
        node9 = TreeNode(val=9)
        node3 = TreeNode(val=3, left=node9, right=node20)
        self.assertEqual(2, Solution().minDepth(node3))


if __name__ == '__main__':
    unittest.main()
