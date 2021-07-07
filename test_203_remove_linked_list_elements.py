import unittest

"""
write down thoughts
1. use dummy head to represent the node before head, so head can be potentially removed if val=val.
2. in the end, need to link prev with the curr, so you don't miss any None or miss the removal of last node (if val=val)
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        prev.next = curr
        return dummy.next


class TestSolution(unittest.TestCase):
    def test1(self):
        node61 = ListNode(val=6)
        node5 = ListNode(val=5,next=node61)
        node4 = ListNode(val=4,next=node5)
        node3 = ListNode(val=3,next = node4)
        node62 = ListNode(val=6,next=node3)
        node2 = ListNode(val=2,next=node62)
        node1 = ListNode(val=1,next=node2)
        head = Solution().removeElements(node1, 6)
        self.assertEqual(1, head.val)
        self.assertEqual(2, head.next.val)
        self.assertEqual(3, head.next.next.val)
        self.assertEqual(4, head.next.next.next.val)
        self.assertEqual(5, head.next.next.next.next.val)
        self.assertEqual(None, head.next.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
