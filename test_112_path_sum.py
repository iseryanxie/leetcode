import unittest

"""
write down thoughts
recursion, test hasPathSum(sum-node.val,node.left) or hasPathSum(sum-node.val,node.right)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        # only test for ==, because there are positive and negative numbers
        if targetSum==root.val and not root.left and not root.right: # leaf node value equals sum
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)



class TestSolution(unittest.TestCase):
    def test1(self):
        node1 = TreeNode(val=1)
        node2 = TreeNode(val=2)
        node7 = TreeNode(val=7)
        node11 = TreeNode(val=11, left=node7, right=node2)
        node4r = TreeNode(val=4, right=node1)
        node13 = TreeNode(val=13)
        node4l = TreeNode(val=4, left=node11)
        node8 = TreeNode(val=8, left=node13, right=node4r)
        node5 = TreeNode(val=5, left=node4l, right=node8)
        self.assertEqual(True, Solution().hasPathSum(node5, 22))

    def test2(self):
        node2 = TreeNode(val=2)
        node3 = TreeNode(val=3)
        node1 = TreeNode(val=1, left=node2, right=node3)
        self.assertEqual(False, Solution().hasPathSum(node1, 5))

    def test3(self):
        self.assertEqual(False, Solution().hasPathSum(None, 0))

    def test4(self):
        node2 = TreeNode(val=2)
        node1 = TreeNode(val=1, left=node2)
        self.assertEqual(False, Solution().hasPathSum(node1, 1))

    def test5(self):
        node2 = TreeNode(val=-3)
        node1 = TreeNode(val=-2, right=node2)
        self.assertEqual(True, Solution().hasPathSum(node1, -5))

if __name__ == '__main__':
    unittest.main()
