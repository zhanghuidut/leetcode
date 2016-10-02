# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ptemp = None
        while l1 and l2:
            if l1.val < l2.val:
                if not ptemp:
                    head = ptemp = l1
                else:
                    ptemp.next = l1
                    ptemp = l1
                l1 = l1.next
            else:
                if not ptemp:
                    head = ptemp = l2
                else:
                    ptemp.next = l2
                    ptemp = l2
                l2 = l2.next

        while l1:
            if not ptemp:
                head = ptemp = l1
            else:
                ptemp.next = l1
                ptemp = l1
            l1 = l1.next

        while l2:
            if not ptemp:
                head = ptemp = l2
            else:
                ptemp.next = l2
                ptemp = l2
            l2 = l2.next
        
        return head
        
