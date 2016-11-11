# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cur, temp = head, head.next
        while temp:
            if temp.val != cur.val:
                cur.next = temp
                cur = cur.next
            temp = temp.next
        cur.next = temp
        return head
