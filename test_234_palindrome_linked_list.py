# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # slow = fast = head
        # while fast != None and fast.next != None:
        #     slow = slow.next
        #     fast = fast.next.next
        # if fast != None:  # case number of elements is odd, move mid to next element.
        #     slow = slow.next
        #
        # def reverse(head):
        #     ans = None
        #     while head != None:
        #         next = head.next
        #         head.next = ans
        #         ans = head
        #         head = next
        #     return ans
        #
        # head2 = reverse(slow)  # slow is our mid
        # while head2 != None:
        #     if head.val != head2.val:
        #         return False
        #     head = head.next
        #     head2 = head2.next
        # return True
        slow = head
        fast = head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        if fast != None:  # case number of elements is odd, move mid to next element.
            slow = slow.next

        def reverse(head):  # 3->2->1->None
            ans = None  # new reversed linked list
            while head is not None:
                next = head.next  # 2
                if next != None:
                    print("1step", next.val)
                head.next = ans  # 3->None
                if ans != None:
                    print("2step", ans.val)
                ans = head  # ans=3->None
                if ans != None:
                    print("3step", ans.val)
                head = next # next.val = 2, next.next.val=1
                if (head != None):
                    print("4step", head.val)
            return ans

        head2 = reverse(slow)
        while head2 is not None:
            if head2.val != head.val:
                return False
            head2 = head2.next
            head = head.next
        return True


# 1->2->3->3->2->1->None
node6 = ListNode(1)
node5 = ListNode(2, node6)
node4 = ListNode(3, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
ans = Solution().isPalindrome(head)
print(ans)
