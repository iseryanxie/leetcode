import unittest

"""
write down thoughts
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def btPath(prefix, node):
            if not node.left and not node.right:
                res.append(prefix + str(node.val))
                return  # finish recursion at leaf node
            if node.left:
                btPath(prefix + str(node.val) + '->', node.left)
            if node.right:
                btPath(prefix + str(node.val) + '->', node.right)

        btPath("", root)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        node5 = TreeNode(val=5)
        node2 = TreeNode(val=2, right=node5)
        node3 = TreeNode(val=3)
        node1 = TreeNode(val=1, left=node2, right=node3)
        self.assertEqual(["1->2->5", "1->3"], Solution().binaryTreePaths(node1))


if __name__ == '__main__':
    unittest.main()
