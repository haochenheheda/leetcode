class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend * divisor > 0:
        	flag = 1
        else:
        	flag = -1
        
        re = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while True:
        	divisor1 = divisor
        	if divisor1 <= dividend:
        		s = 0
        		while divisor1 << 1 <= dividend:
        			divisor1 = divisor1 << 1
        			s += 1
        		re += 1 << s
        		dividend -= divisor1
        	else:
        		break

        return min(max(re * flag,-1<<31),(1<<31)-1)

if __name__ == '__main__':
	s = Solution()
	print(s.divide(1000,1))