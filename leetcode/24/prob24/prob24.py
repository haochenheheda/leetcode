# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s_flag = False
        head_ = ListNode(0)
        head_.next = head
        tmp__ = head_
        p = head
        while p != None:
        	if not s_flag:
        		tmp_ = p
        		p = p.next
        	else:
        		# print(tmp__.val,p.val,tmp_.val)
        		tmp__.next = p
        		n = p.next
        		p.next = tmp_
        		tmp__ = tmp_
        		tmp_.next = n
        		p = n
        	s_flag = not s_flag
        return head_.next

if __name__ == '__main__':
	s = Solution()
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	re = s.swapPairs(head)
	while re != None:
		print(re.val)
		re = re.next
