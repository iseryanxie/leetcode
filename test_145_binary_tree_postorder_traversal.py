import unittest

"""
write down thoughts
dfs on postorder left,right,node
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node,list):
            if node is None:
                return
            dfs(node.left,list)
            dfs(node.right,list)
            list.append(node.val)
        res = []
        if root is None:
            return res
        dfs(root,res)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        node3 = TreeNode(val=3)
        node2 = TreeNode(val=2, left=node3)
        node1 = TreeNode(val=1, right=node2)
        self.assertEqual([3,2,1], Solution().postorderTraversal(node1))


if __name__ == '__main__':
    unittest.main()
