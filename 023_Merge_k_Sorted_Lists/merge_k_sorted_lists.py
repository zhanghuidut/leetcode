#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ptemp = None
        lists = filter(lambda x: x, lists)
        if not lists:
            return
        self.buildheap(lists)
        while 1:
            if len(lists) == 1:
                if ptemp == None:
                    head = ptemp = lists[0]
                else:
                    ptemp.next = lists[0]
                return head
            else:
                tmp = lists[0]
                lists[0] = lists[0].next or lists.pop()
                self.heapfy(lists, 0)

                if ptemp == None:
                    head = ptemp = tmp
                else:
                    ptemp.next = tmp
                    ptemp = tmp

        return head

    def buildheap(self, lists):
        nums = len(lists)
        for i in range(nums/2-1, -1, -1):
            self.heapfy(lists, i)

    def heapfy(self, lists, n):
        left, right, num = 2*n+1, 2*n+2, len(lists)
        if left < num and lists[left].val < lists[n].val:
            minval = left
        else:
            minval = n
        
        if right < num and lists[right].val < lists[minval].val:
            minval = right
        
        if minval != n:
            lists[n], lists[minval] = lists[minval], lists[n]
            self.heapfy(lists, minval)
