import unittest

"""
write down thoughts
- use the property of BST: left subtree is smaller than root and right subtree is larger than root
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:  # if need to split, then it's LCA node OR any of them equals, it's also LCA
                return curr


class TestSolution(unittest.TestCase):
    def test1(self):
        node0 = TreeNode(0)
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node4.left = node3
        node4.right = node5
        node2 = TreeNode(2)
        node2.left = node0
        node2.right = node4
        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node8 = TreeNode(8)
        node8.left = node7
        node8.right = node9
        node6 = TreeNode(6)
        node6.left = node2
        node6.right = node8
        self.assertEqual(node6, Solution().lowestCommonAncestor(node6, node2, node8))
        self.assertEqual(node6, Solution().lowestCommonAncestor(node6, node7, node4))
        self.assertEqual(node8, Solution().lowestCommonAncestor(node6, node7, node9))


if __name__ == '__main__':
    unittest.main()
