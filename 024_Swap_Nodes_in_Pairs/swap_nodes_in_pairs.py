# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        start = ListNode(0)
        start.next = head

        slow, fast = start ,head.next
        while fast:
            slow.next.next = fast.next
            fast.next = slow.next
            slow.next = fast
            slow = slow.next.next
            try:
                fast = slow.next.next
            except AttributeError:
                break
        
        return start.next
        
