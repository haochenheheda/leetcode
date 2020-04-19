class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        flag = True
        for i in s:
        	if i == '(' or i == '[' or i == '{':
        		stack.append(i)
        	elif len(stack) > 0 and ((i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{')):
        		stack.pop(-1)
        	else:
        		flag = False
        		break
        return flag and stack == []

if __name__ == '__main__':
	s = Solution()
	str_ = '['
	print(s.isValid(str_))