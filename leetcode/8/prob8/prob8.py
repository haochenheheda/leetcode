class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_ = str.strip()
        if len(str_) == 0:
        	return 0
        re = ''
        if str_[0] == '+' or str_[0] == '-' or (ord(str_[0]) >= 48 and ord(str_[0]) <= 57):
        	re += str_[0]
        	if str_[0] == '+' or str_[0] == '-':
        		re += '0'
        	for s in str_[1:]:
        		if ord(s) < 48 or ord(s) > 57:
        			break
        		else:
        			re += s
        	re = int(re)
        	if re > 2 ** 31 - 1:
        		return 2 ** 31 - 1
        	elif re < - 2 ** 31:
        		return - 2 ** 31

        	return re
        else:
        	return 0
if __name__ == '__main__':
	s = Solution()
	x = "+"
	print(s.myAtoi(x))