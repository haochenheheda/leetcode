class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_ = {1:['I','V'],2:['X','L'],3:['C','D'],4:['M',None]}
        re = ''
        for i in range(1,5):
        	if num == 0:
        		break
        	tmp = num % 10
        	num = num / 10
        	one,five = dict_[i]
        	if tmp < 4:
        		re += one * tmp
        	elif tmp == 4:
        		re += (five + one)
        	elif tmp < 9:
        		re += (one * (tmp-5) + five)
        	else:
        		ten = dict_[i+1][0]
        		re += (ten + one)
        return re[::-1]


if __name__ == '__main__':
	s = Solution()
	print(s.intToRoman(1994))