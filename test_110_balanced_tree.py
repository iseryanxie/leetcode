import unittest

"""
write down thoughts
have an additional output of the recursive function to globally set status of is_balance. 
otherwise keep the max depth of a subtree to compare.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        global result
        result = True
        def rec_search(root):
            """return the max depth of subtree"""
            global result
            if not root:
                return 0
            left = 1+rec_search(root.left)
            right = 1+rec_search(root.right)
            if abs(left-right)>1:
                result = False
            return max(left,right)
        rec_search(root)
        return result


class TestSolution(unittest.TestCase):
    def test1(self):
        node15 = TreeNode(val=15)
        node7 = TreeNode(val=7)
        node20 = TreeNode(val=20,left=node15,right=node7)
        node9 = TreeNode(val=9)
        node3 = TreeNode(val=3,left=node9,right=node20)
        self.assertEqual(True, Solution().isBalanced(node3))


if __name__ == '__main__':
    unittest.main()
