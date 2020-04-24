class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
        	return 0
        for i in range(len(haystack)-len(needle)+1):
        	if haystack[i:i+len(needle)] == needle:
        		return i
        return -1


if __name__ == '__main__':
	h = 'hello'
	n = 'll'
	s = Solution()
	print(s.strStr(h,n))