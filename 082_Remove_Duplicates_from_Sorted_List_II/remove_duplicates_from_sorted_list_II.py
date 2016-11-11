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
        start = ListNode(0)
        start.next = head

        pre, cur, temp = start, head, head
        while temp:
            if temp != head and temp.val == cur.val:
                temp = temp.next
            else:
                cur = temp
                if (not temp.next) or (temp.val != temp.next.val):
                    pre.next = temp
                    pre = temp
                temp = temp.next
        pre.next = temp
        return start.next
