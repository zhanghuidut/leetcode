# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        
        if not head.next:
            return TreeNode(head.val)
        
        fir, sec = ListNode(0), head
        fir.next = head
        while sec and sec.next:
            sec = sec.next
            sec = sec.next
            fir = fir.next
        
        root = TreeNode(fir.next.val)
        tmp = fir.next.next
        fir.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp)
        
        return root
