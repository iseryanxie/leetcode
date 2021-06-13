import unittest

"""
write down thoughts
keep track of first and previous node, find next unique value then link to previous node,
update previous node, keep going
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        first = head
        previous = head
        if head is None:
            return None
        curr = head.next
        while curr:
            if curr.val == previous.val:

                curr = curr.next
                continue
            previous.next = curr
            previous = curr
            curr = curr.next
        previous.next = curr
        return first


class TestSolution(unittest.TestCase):
    def test1(self):
        Node1 = ListNode(val=3)
        Node2 = ListNode(val=3,next=Node1)
        Node3 = ListNode(val=2,next=Node2)
        Node4 = ListNode(val=1,next=Node3)
        Node5 = ListNode(val=1, next=Node4)
        uniqueNode = Solution().deleteDuplicates(Node5)
        self.assertEqual(1,uniqueNode.val)
        self.assertEqual(2, uniqueNode.next.val)
        self.assertEqual(3, uniqueNode.next.next.val)
        self.assertEqual(None,uniqueNode.next.next.next)


if __name__ == '__main__':
    unittest.main()
