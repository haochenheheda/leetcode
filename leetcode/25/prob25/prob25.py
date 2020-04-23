# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
        	return head
        size = 0
        tmp = head
        while tmp != None:
        	size += 1
        	tmp = tmp.next
        t = size/k*k
        head_ = ListNode(0)
        head_.next = head
        prev = head_
        p = head
        t_ = 1
        while t_ <= t:
        	if t_% k == 1:
        		next_prev = p
        	nxt = p.next
        	n = prev.next
        	prev.next = p
        	p.next = n
        	p = nxt
        	if t_%k == 0:
        		prev = next_prev
        	t_ += 1
        prev.next = p
        return head_.next

if __name__ == '__main__':
	s = Solution()
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	re = s.reverseKGroup(head,1)
	while re != None:
		print(re.val)
		re = re.next