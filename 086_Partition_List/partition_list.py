# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        start = pre = cur = ListNode(0)
        start.next = head
        while cur and cur.next:
            if cur.next.val < x:
                if pre != cur:
                    temp = pre.next
                    pre.next = cur.next
                    pre = pre.next
                    cur.next = cur.next.next
                    pre.next = temp
                else:
                    pre = pre.next
                    cur = cur.next
            else:
                cur = cur.next
            
        return start.next
