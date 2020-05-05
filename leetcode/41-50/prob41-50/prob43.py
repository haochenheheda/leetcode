class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ind1 = 0
        ind2 = 0
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        re = 0
        for ind1 in range(len(num1)):
        	for ind2 in range(len(num2)):
        		n1 = int(num1[l1-ind1])
        		n2 = int(num2[l2-ind2])
        		re += n1*n2*10**(ind1+ind2)
        return str(re)


if __name__ == '__main__':
	s = Solution()
	print(s.multiply('123','456'))