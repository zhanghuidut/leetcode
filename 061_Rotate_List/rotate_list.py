# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head is None:
            return head
        
        temp, fast, slow = head, head, head

        n = 0
        while temp:
            n += 1
            temp = temp.next
        k %= n

        for i in range(k):
            try:
                fast = fast.next
            except :
                return head

        if fast is None:
            return head
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head
        new_start = slow.next
        slow.next = None
        
        return new_start

            
