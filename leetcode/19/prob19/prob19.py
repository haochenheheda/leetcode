# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(None)
        p.next = head
        if head.next == None:
        	return None
        p_ = p
        tmp = p
        for i in range(n+1):
        	tmp = tmp.next
        while tmp != None:
        	p_ = p_.next
        	tmp = tmp.next
        p_.next = p_.next.next
        return p.next
if __name__ == '__main__':
	s = Solution()
	lst = [1,2]
	for i in range(len(lst)-1,-1,-1):
		if i == len(lst) - 1:
			node = ListNode(lst[i])
		else:
			next_node = node
			node = ListNode(lst[i])
			node.next = next_node
	head = s.removeNthFromEnd(node,2)
	while head != None:
		print(head.val)
		head = head.next

