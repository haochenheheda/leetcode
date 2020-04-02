# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        t = r
        tmp = 0
        while True:
            if l1 != None and l2 != None:
                this_value = (l1.val + l2.val + tmp)%10
                tmp = (l1.val + l2.val + tmp)/10
                l1 = l1.next
                l2 = l2.next
                t.next = ListNode(this_value)
                t = t.next
            elif l1 == None and l2 != None:
                this_value = (l2.val + tmp)%10
                tmp = (l2.val + tmp)/10
                l2 = l2.next
                t.next = ListNode(this_value)
                t = t.next
            elif l1 != None and l2 == None:
                this_value = (l1.val + tmp)%10
                tmp = (l1.val + tmp)/10
                l1 = l1.next
                t.next = ListNode(this_value)
                t = t.next
            else:
            	if tmp != 0:
            		t.next = ListNode(tmp)
            	break
        return r.next      


if __name__ == '__main__':
	s = Solution()
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	r = s.addTwoNumbers(l1,l2)
	while r != None:
		print(r.val)
		r = r.next
