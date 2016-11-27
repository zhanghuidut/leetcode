# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        sec = slow.next
        slow.next = last = None
        while sec.next:
            temp = sec.next
            sec.next = last
            last = sec
            sec = temp
        sec.next = last

        fir = head
        while sec:
            temp1 = fir.next
            temp2 = sec.next
            fir.next = sec
            sec.next = temp1
            fir = temp1
            sec = temp2
    
        