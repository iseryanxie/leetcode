import unittest

"""
write down thoughts
replace the to-be-deleted node with its next node (value and next).
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next


class TestSolution(unittest.TestCase):
    def test1(self):
        node9 = ListNode(x=9)
        node1 = ListNode(x=1)
        node1.next = node9
        node5 = ListNode(5)
        node5.next = node1
        node4 = ListNode(4)
        node4.next = node5
        Solution().deleteNode(node5)
        self.assertEqual(4, node4.val)
        self.assertEqual(1,node4.next.val)
        self.assertEqual(9,node4.next.next.val)
        self.assertEqual(None,node4.next.next.next)


if __name__ == '__main__':
    unittest.main()
