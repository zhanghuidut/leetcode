# iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        start, cur = head, head.next
        head.next = None
        while cur:
            temp = cur.next
            cur.next = start
            start = cur
            cur = temp

        return start

# recursively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        head, tail = self.reverse(head)
        return head

    def reverse(self, node):
        if node.next:
            head, temp = self.reverse(node.next)
            temp.next = node
            node.next = None
            return head, node
        else:
            return node, node
