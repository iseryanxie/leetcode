import unittest

"""
write down thoughts
iterate the linked list, if find node in existing hashmap then True, otherwise add to hashmap
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashmap = {}
        iter = head
        while iter and iter.next:
            if iter.next in hashmap:
                return True
            else:
                iter = iter.next
                hashmap[iter] = True
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        node0 = ListNode(x=0)
        node4 = ListNode(x=4)
        node2 = ListNode(x=2)
        node3 = ListNode(x=3)
        node3.next = node2
        node2.next = node0
        node0.next = node4
        node4.next = node2
        self.assertEqual(True, Solution().hasCycle(node3))


if __name__ == '__main__':
    unittest.main()
