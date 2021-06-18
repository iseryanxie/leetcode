import unittest

"""
write down thoughts
Recursive:
check current node val, then check if left of left equal right of right AND right of left equal left of right
Iterative:
put all the values of the same level of tree in a list, then check list==list[::-1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isEqual(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and isEqual(left.left, right.right) and isEqual(left.right, right.left)

        return isEqual(root.left, root.right)

#
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         queue = [root]
#         while queue: # stop if th next level is empty
#             nextlevel = []
#             for node in queue:
#                 if node == None:
#                     continue
#                 # build a list of TreeNode for the next level
#                 nextlevel.append(node.left)
#                 nextlevel.append(node.right)
#             # build this level's values into a list
#             thislevel = [node.val if node != None else None for node in queue]
#             if thislevel != thislevel[::-1]:
#                 return False
#             queue = nextlevel
#         return True


class TestSolution(unittest.TestCase):
    def test1(self):
        node_left5 = TreeNode(val=5)
        node_left3 = TreeNode(val=3, left=node_left5)
        node_left4 = TreeNode(val=4)
        node_left2 = TreeNode(val=2, left=node_left3, right=node_left4)
        node_right3 = TreeNode(val=3)
        node_right4 = TreeNode(val=4)
        node_right2 = TreeNode(val=2, left=node_right4, right=node_right3)
        node_1 = TreeNode(val=1, left=node_left2, right=node_right2)
        self.assertEqual(False, Solution().isSymmetric(node_1))

    def test2(self):
        node_left3 = TreeNode(val=3)
        node_left4 = TreeNode(val=4)
        node_left2 = TreeNode(val=2, left=node_left3, right=node_left4)
        node_right3 = TreeNode(val=3)
        node_right4 = TreeNode(val=4)
        node_right2 = TreeNode(val=2, left=node_right4, right=node_right3)
        node_1 = TreeNode(val=1, left=node_left2, right=node_right2)
        self.assertEqual(True, Solution().isSymmetric(node_1))


if __name__ == '__main__':
    unittest.main()
