# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid, slow, fast = head, head, head
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None  # left list start from head to slow->None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.val < right.val:
            head = ListNode(left.val) # left.val is the smallest number of both list, left.val-> rest of the group
            # then call merge recursively on the rest of the list
            head.next = self.merge(left.next, right)
        else:
            head = ListNode(right.val)
            head.next = self.merge(left, right.next)
        return head


# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#
#         if not head or not head.next:
#             return head
#         pre, slow, fast = head, head, head
#         while fast and fast.next:  # 找链表中点
#             pre = slow
#             slow = slow.next
#             fast = fast.next.next
#
#         pre.next = None
#         left, right = self.sortList(head), self.sortList(slow)
#         return self.merge(left, right)
#
#     def merge(self, l1, l2):
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#
#         if l1.val < l2.val:
#             head = ListNode(l1.val)
#             head.next = self.merge(l1.next, l2)
#         else:
#             head = ListNode(l2.val)
#             head.next = self.merge(l1, l2.next)
#         return head


# 4->3->2->1->None
node5 = ListNode(3)
node4 = ListNode(5,node5)
node3 = ListNode(6, node4)
node2 = ListNode(4, node3)
head = ListNode(2, node2)
ans = Solution().sortList(head)
while ans != None:
    print(ans.val)
    ans = ans.next
