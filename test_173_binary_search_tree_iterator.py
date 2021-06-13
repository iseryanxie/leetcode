import unittest

"""
write down thoughts
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = [] # create a stack
        self.pushLeft(root) # push all the nodes on the left of root node to stack with pushLeft method

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        popedNode = self.stack.pop() # pop current node
        self.pushLeft(popedNode.right) # push all the node that is on the left branch of the current node to stack with pushleft method
        return popedNode.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) != 0

    def pushLeft(self, node):
        while (node): # while still not empty
            self.stack.append(node) # push node to stack
            node = node.left # move to the left of the node and continue this process


class TestSolution(unittest.TestCase):
    def test1(self):
        leaf20 = TreeNode(val=20)
        leaf9 = TreeNode(val=9)
        branch1 = TreeNode(val=3)
        branch2 = TreeNode(val=15, left=leaf9, right=leaf20)
        root = TreeNode(val=7, left=branch1, right=branch2)
        bst = BSTIterator(root)
        self.assertEqual(3, bst.next())  # return 3
        self.assertEqual(7, bst.next())  # return 7
        self.assertEqual(True, bst.hasNext())  # return True
        self.assertEqual(9, bst.next())  # return 9
        self.assertEqual(True, bst.hasNext())  # return True
        self.assertEqual(15, bst.next())  # return 15
        self.assertEqual(True, bst.hasNext())  # return True
        self.assertEqual(20, bst.next())  # return 20
        self.assertEqual(False, bst.hasNext())  # return False


if __name__ == '__main__':
    unittest.main()
