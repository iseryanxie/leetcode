import unittest

"""
write down thoughts
merge sort
"""

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = l1
        r = l2
        dummy_head=dummy_node = ListNode(0)
        while l or r:
            if l and r:
                if l.val<=r.val:
                    dummy_node.next = l # change to ListNode(val=l.val) to replace
                    l = l.next
                else:
                    dummy_node.next = r # ListNode(val=r.val)
                    r = r.next
            elif l:
                dummy_node.next = l # ListNode(val=l.val)
                l = l.next
            elif r:
                dummy_node.next = r # ListNode(val=r.val)
                r = r.next
            dummy_node = dummy_node.next
            # note that dummy_node is a reference to existing nodes, either l or r
            # dummy_node.next is changed to existing linked list
        return dummy_head.next


class TestSolution(unittest.TestCase):
    def test1(self):
        node14 = ListNode(val=4)
        node12 = ListNode(val=2,next=node14)
        node11 = ListNode(val=1,next=node12)
        node24 = ListNode(val=4)
        node23 = ListNode(val=3,next=node24)
        node21 = ListNode(val=1,next=node23)
        res = Solution().mergeTwoLists(node11, node21)
        self.assertEqual(1, res.val)
        self.assertEqual(1, res.next.val)
        self.assertEqual(2, res.next.next.val)
        self.assertEqual(3, res.next.next.next.val)
        self.assertEqual(4, res.next.next.next.next.val)
        self.assertEqual(4, res.next.next.next.next.next.val)
        self.assertEqual(None, res.next.next.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
