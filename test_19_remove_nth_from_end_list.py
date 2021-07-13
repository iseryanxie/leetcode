import unittest

"""
write down thoughts
1. Two pass is easy. First pass to record the full length, then remove the L-n node.
2. Need only one pass.
use two pointers, one pointer moves n in the begining. Then both pointer moves in the same pace, until the first pointer
find the end, the second pointer removes the node.
use dummy node to keep the head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(next=head)
        first=second = dummy
        for _ in range(n+1):
            first = first.next # we can assume n<sz according to the problem statement
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


class TestSolution(unittest.TestCase):
    def test1(self):
        node5 = ListNode(5)
        node4 = ListNode(4,node5)
        node3 = ListNode(3,node4)
        node2 = ListNode(2,node3)
        node1 = ListNode(1,node2)
        res = Solution().removeNthFromEnd(node1, 2)
        self.assertEqual(1, res.val)
        self.assertEqual(2, res.next.val)
        self.assertEqual(3, res.next.next.val)
        self.assertEqual(5, res.next.next.next.val)
        self.assertEqual(None, res.next.next.next.next)
    def test2(self):
        node1 = ListNode(1)
        res = Solution().removeNthFromEnd(node1, 1)
        self.assertEqual(None, res)


if __name__ == '__main__':
    unittest.main()
