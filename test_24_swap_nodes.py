import unittest

"""
write down thoughts
use fast, slow two pointers to swap. use a prev pointer to link
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        prev = dummy
        if head:
            slow = head
        else:
            return None
        if head.next:
            fast = head.next
        else:
            return head
        while slow and fast:
            prev.next = fast # link prev to fast to swap
            slow.next = fast.next # save the next node of fast first
            fast.next = slow # fast point to slow, now fast is the new slow
            prev = slow # move on to the next iter, prev now point to the new "fast", which is slow
            slow = slow.next # slow is still slow in the next iter by moving 1 step
            if slow:
                fast = slow.next # fast is fast by moving another 1 step, given slow is not None yet
            else:
                break
        return dummy.next



class TestSolution(unittest.TestCase):
    def test1(self):
        node4 = ListNode(4)
        node3 = ListNode(3,node4)
        node2 = ListNode(2,node3)
        node1 = ListNode(1,node2)
        new_node = Solution().swapPairs(node1)
        self.assertEqual(2, new_node.val)
        self.assertEqual(1, new_node.next.val)
        self.assertEqual(4, new_node.next.next.val)
        self.assertEqual(3, new_node.next.next.next.val)
        self.assertEqual(None, new_node.next.next.next.next)
    def test2(self):
        node1 = ListNode(val=1)
        new_node = Solution().swapPairs(node1)
        self.assertEqual(1, new_node.val)
        self.assertEqual(None, new_node.next)
    def test3(self):
        new_node = Solution().swapPairs(None)
        self.assertEqual(None, new_node)


if __name__ == '__main__':
    unittest.main()
