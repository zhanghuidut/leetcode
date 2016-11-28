# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# quick_sort: TLE
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        self.quicksort(start, None)
        return start.next
    
    def quicksort(self, start, tail):
        if start.next and start.next != tail:
            q = self.partion(start, tail)
            self.quicksort(start, q)
            self.quicksort(q, tail)
    
    def partion(self, start, tail):
        val = start.next.val
        pre, cur = start, start
        while cur and cur.next and cur.next != tail:
            if cur.next.val < val:
                if cur != pre:
                    temp = pre.next
                    pre.next = cur.next
                    pre = pre.next
                    cur.next = cur.next.next
                    pre.next = temp
                else:
                    cur = cur.next
                    pre = pre.next
            else:
                cur = cur.next
        return pre.next


# merge sort: AC
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(None)
        start.next = head
        self.mergesort(start)
        return start.next
    
    def mergesort(self, start1):
        if start1.next and start1.next.next:
            fir, sec = start1.next, start1.next.next
            while sec and sec.next:
                fir = fir.next
                sec = sec.next
                sec = sec.next
            mid = fir.next
            fir.next = None
            self.mergesort(start1)
            start2 = ListNode(None)
            start2.next = mid
            self.mergesort(start2)
            self.merge(start1, start2)
    
    def merge(self, start1, start2):
        temp = start1
        fir = start1.next
        sec = start2.next
        while fir != None and sec != None:
            if fir.val < sec.val:
                temp.next = fir
                fir = fir.next
            else:
                temp.next = sec
                sec = sec.next
            temp = temp.next
        
        while fir != None:
            temp.next = fir
            fir = fir.next
            temp = temp.next
        
        while sec != None:
            temp.next = sec
            sec = sec.next
            temp = temp.next
