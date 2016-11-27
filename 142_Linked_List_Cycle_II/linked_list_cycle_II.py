# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        slow, fast = head, head.next
        sign = None
        while fast and fast.next:
            if fast == slow or fast.next == slow:
                sign = slow.next.next
                break

            fast = fast.next
            fast = fast.next
            slow = slow.next

        if not sign:
            return
        temp = head
        while 1:
            if temp == sign:
                return temp
            temp = temp.next
            sign = sign.next
