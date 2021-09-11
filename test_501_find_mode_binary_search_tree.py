import unittest

"""
write down thoughts
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Start by checking the left node of the node 
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        count = 0
        modes = []
        max_occur = 0

        def inorder_traversal(node: Optional[TreeNode]):
            nonlocal prev
            nonlocal max_occur
            nonlocal count
            nonlocal modes
            if not node:
                return
            inorder_traversal(node.left)  # always traverse left node first
            if prev == node.val: # prev has the value of last node
                count += 1
            else: # if prev is not node.val, then restart the count
                count = 1
                prev = node.val
            if count > max_occur:
                max_occur = count
                modes = [prev]
            elif count == max_occur: # return all modes when there are ties
                modes.append(prev)
            inorder_traversal(node.right)

        inorder_traversal(root)
        return modes


class TestSolution(unittest.TestCase):
    def test1(self):
        node2l = TreeNode(val=2)
        node2r = TreeNode(val=2, left=node2l)
        node1 = TreeNode(val=1, right=node2r)
        self.assertEqual([2], Solution().findMode(node1))

    def test2(self):
        node0 = TreeNode(val=0)
        self.assertEqual([0], Solution().findMode(node0))


if __name__ == '__main__':
    unittest.main()
