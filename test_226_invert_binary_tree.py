import unittest

"""
write down thoughts
recursively invert the tree nodes,
swap the two nodes in a single step to avoid loss of nodes
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class TestSolution(unittest.TestCase):
    def test1(self):
        node1 = TreeNode(val=1)
        node3 = TreeNode(val=3)
        node2 = TreeNode(val=2, left=node1, right=node3)
        node6 = TreeNode(val=6)
        node9 = TreeNode(val=9)
        node7 = TreeNode(val=7, left=node6, right=node9)
        node4 = TreeNode(val=4, left=node2, right=node7)
        invert = Solution().invertTree(node4)
        self.assertEqual(4, invert.val)
        self.assertEqual(7, invert.left.val)
        self.assertEqual(2, invert.right.val)
        self.assertEqual(9, invert.left.left.val)


if __name__ == '__main__':
    unittest.main()
