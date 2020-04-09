class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)

if __name__ == '__main__':
	s = Solution()
	str_ = '121'
	print(s.isPalindrome(str_))
