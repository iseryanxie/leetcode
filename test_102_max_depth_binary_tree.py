import unittest

"""
write down thoughts
recursion: max = 1+ max(max_depth(left),max_depth(right))
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))


class TestSolution(unittest.TestCase):
    def test1(self):
        node15 = TreeNode(val=15)
        node7 = TreeNode(val=7)
        node20 = TreeNode(val=20,left=node15,right=node7)
        node9 = TreeNode(val=9)
        node3 = TreeNode(val=3,left=node9,right=node20)
        self.assertEqual(3, Solution().maxDepth(node3))


if __name__ == '__main__':
    unittest.main()
