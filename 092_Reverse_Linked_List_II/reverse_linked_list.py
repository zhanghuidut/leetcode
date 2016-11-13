class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        for i in range(m):
            if i == m-1:
                first, last = self.reverse(start.next, n-m)
                start.next = first
            else:
                start = start.next

        return start.next if m == 1 else head
    
    def reverse(self, start, k):
        last, cur = start, start.next
        for i in range(k):
            temp = cur.next
            cur.next = start
            start = cur
            cur = temp
        last.next = cur
        return start, last
