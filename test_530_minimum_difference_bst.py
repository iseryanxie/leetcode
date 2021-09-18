import unittest

"""
write down thoughts
use in-order traversal to sort the list, then find the minimal difference in the sorted list.
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(root, output):
            if not root:
                return
            inorder_traversal(root.left,output)
            output.append(root.val)
            inorder_traversal(root.right,output)
        output = []
        inorder_traversal(root,output)
        min_diff = None
        for i in range(1,len(output)):
            if min_diff == None:
                min_diff = output[i]-output[i-1]
            else:
                min_diff = min(min_diff, output[i]-output[i-1])
        return min_diff


class TestSolution(unittest.TestCase):
    def test1(self):
        node1 = TreeNode(val=1)
        node3 = TreeNode(val=3)
        node2 = TreeNode(val=2, left=node1, right=node3)
        node6 = TreeNode(val=6)
        node4 = TreeNode(val=4,left=node2,right=node6)
        self.assertEqual(1, Solution().getMinimumDifference(node4))


if __name__ == '__main__':
    unittest.main()
