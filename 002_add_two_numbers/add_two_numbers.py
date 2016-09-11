# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        result = ptemp = None
        while (l1 and l2):
            val = l1.val + l2.val + flag
            flag = 1 if val >= 10 else 0
            temp = ListNode(val%10)
            if ptemp:
                ptemp.next = temp
            else:
                ptemp = temp
                result = ptemp
            l1 = l1.next
            l2 = l2.next
            ptemp = temp
        
        while l1:
            val = l1.val + flag
            flag = 1 if val >= 10 else 0
            temp = ListNode(val%10)
            ptemp.next = temp
            ptemp = temp
            l1 = l1.next
        
        while l2:
            val = l2.val + flag
            flag = 1 if val >= 10 else 0
            temp = ListNode(val%10)
            ptemp.next = temp
            ptemp = temp
            l2 = l2.next
        if flag:
            temp = ListNode(1)
            ptemp.next = temp
        return result
