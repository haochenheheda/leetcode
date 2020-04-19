# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        head_ = head
        while l1 != None and l2 != None:
        	if l1.val < l2.val:
        		t = ListNode(l1.val)
        		head_.next = t
        		head_ = head_.next
        		l1 = l1.next
        	else:
        		t = ListNode(l2.val)
        		head_.next = t
        		head_ = head_.next
        		l2 = l2.next
        if l1 != None:
        	head_.next = l1
        if l2 != None:
        	head_.next = l2
        return head.next        		

if __name__ == '__main__':
	s = Solution()
	lst1 = [1,2,4]
	lst2 = [1,3,4]
	for ind in range(len(lst1)-1,-1,-1):
		t = ListNode(lst1[ind])
		if ind < len(lst1) - 1:
			t.next = tt
		tt = t
	head1 = tt
	for ind in range(len(lst2)-1,-1,-1):
		t = ListNode(lst2[ind])
		if ind < len(lst2) - 1:
			t.next = tt
		tt = t
	head2 = tt
	r = s.mergeTwoLists(head1,head2)
	while r != None:
		print(r.val)
		r = r.next