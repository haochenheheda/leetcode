class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
        	return s
        s_lst = [''] * numRows
        tmp_row = 0
        ind = 0
        up = True
        for i in range(len(s)):

        	s_lst[tmp_row] += s[i]
        	if tmp_row == (numRows - 1):
        		up = False
        	if tmp_row == 0:
        		up = True
        	if up:
        		tmp_row += 1
        	else:
        		tmp_row -= 1
        re = ''.join(s_lst)
        return re

if __name__ == '__main__':
	s = Solution()
	str_ = "AB"
	rows = 1
	print(s.convert(str_,rows))