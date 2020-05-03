class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        if n == 1:
        	return num
        else:
        	for i in range(1,n):
        		tmp = ''
        		num += 'x'
        		x = 1
        		for j in range(1,len(num)):
        			if num[j] != num[j-1]:
        				tmp += (str(x) + num[j-1])
        				x = 1
        			else:
        				x += 1
        		num = tmp
        	return num


if __name__ == '__main__':
	s = Solution()
	print(s.countAndSay(5))