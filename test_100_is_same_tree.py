import unittest

"""
write down thoughts
recursion
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            if not q:
                return True
            else:
                return False
        if not q:
            if p:
                return False
        return (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


class TestSolution(unittest.TestCase):
    def test1(self):
        node3 = TreeNode(val=3)
        node2 = TreeNode(val=2)
        node1 = TreeNode(val=1,left=node2,right=node3)
        node6 = TreeNode(val=3)
        node5 = TreeNode(val=2)
        node4 = TreeNode(val=1, left=node5, right=node6)
        self.assertEqual(True, Solution().isSameTree(node1,node4))


if __name__ == '__main__':
    unittest.main()
