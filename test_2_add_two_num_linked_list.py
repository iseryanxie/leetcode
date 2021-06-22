import unittest

"""
write down thoughts
since nodes are in reversed order, just need to add from beginning to end
- check exist for each list and carry digits
- need a dummy head (template)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = tail = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0
            tail.next = ListNode(val=sum)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next


class TestSolution(unittest.TestCase):
    def test1(self):
        node3 = ListNode(val=3)
        node4 = ListNode(val=4, next=node3)
        node2 = ListNode(val=2, next=node4)
        node7 = ListNode(val=7)
        node6 = ListNode(val=6, next=node7)
        node5 = ListNode(val=5, next=node6)
        sum = Solution().addTwoNumbers(node2, node5)
        self.assertEqual(7, sum.val)
        self.assertEqual(0, sum.next.val)
        self.assertEqual(1, sum.next.next.val)
        self.assertEqual(1, sum.next.next.next.val)


if __name__ == '__main__':
    unittest.main()
