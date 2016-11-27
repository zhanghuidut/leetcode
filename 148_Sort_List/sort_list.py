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



def buildlist(nums):
    root = temp = None
    for val in nums:
        if temp:
            temp.next = ListNode(val)
            temp = temp.next
        else:
            temp = ListNode(val)
            root = temp

    return root

nums=[3,2,1]
root = buildlist(nums)
Solution().sortList(root)