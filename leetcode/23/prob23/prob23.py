# Definition for singly-linked list.
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
        if len(lists) == 0:
        	return None
        if len(lists) == 1:
        	return lists[0]
        l = 0
        r = len(lists) - 1
        m = (l + r)/2
        l1 = self.mergeKLists(lists[:m+1])
        l2 = self.mergeKLists(lists[m+1:])
        return self.merge(l1,l2)
    def merge(self,l1,l2):
    	head = ListNode(0)
    	tmp = head
    	while l1 != None and l2 != None:
    		if l1.val < l2.val:
    			tmp.next = l1
    			tmp = tmp.next
    			l1 = l1.next
    		else:
    			tmp.next = l2
    			tmp = tmp.next
    			l2 = l2.next    			
    	if l1 != None:
    		tmp.next = l1
    	if l2 != None:
    		tmp.next = l2
    	return head.next

if __name__ == '__main__':
	s = Solution()
	h1 = ListNode(1)
	h1.next = ListNode(4)
	h1.next.next = ListNode(5)

	h2 = ListNode(1)
	h2.next = ListNode(3)
	h2.next.next = ListNode(4)
	
	h3 = ListNode(2)
	h3.next = ListNode(4)
	h3.next.next = ListNode(6)

	r = s.mergeKLists([h1,h2,h3])

	while r != None:
		print(r.val)
		r = r.next
	