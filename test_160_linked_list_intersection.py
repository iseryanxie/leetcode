import unittest

"""
write down thoughts
set two pointers, traverse in both pointers, when one list is exhausted, set it to traverse on another. In this case,
both pointers are traversing the whole two linked list (the intersections are traversed exact two times). Therefore, 
they will either meet at the intersection or null when there is no intersection.
For example, suppose two intersected lists
A->B->C->F->G
   D->E->F->G
   
The traversal of the first pointer is
A->B->C->F->G->D->E->F->G
Second Pointer is
D->E->F->G->A->B->C->F->G
Note that they will meet at the start of the second intersection, by that time, both linked lists almost traversed two 
times (before start of the intersection)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1!=p2:
            if p1 is not None:
                p1 = p1.next
            else:
                p1 = headB

            if p2 is not None:
                p2 = p2.next
            else:
                p2 = headA

        return p2


class TestSolution(unittest.TestCase):
    def test1(self):
        node5 = ListNode(x=5)
        node4 = ListNode(x=4)
        node4.next = node5
        node8 = ListNode(x=8)
        node8.next = node4
        nodeb1 = ListNode(x=1)
        nodeb1.next = node8
        nodea1 = ListNode(x=1)
        nodea1.next = node8
        nodea4 = ListNode(x=4)
        nodea4.next=nodea1
        nodeb6 = ListNode(x=6)
        nodeb6.next=nodeb1
        nodeb5 = ListNode(x=5)
        nodeb5.next=nodeb6
        inters = Solution().getIntersectionNode(nodea4, nodeb5)
        self.assertEqual(8, inters.val)


if __name__ == '__main__':
    unittest.main()
