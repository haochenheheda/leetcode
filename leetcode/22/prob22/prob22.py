class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.dfs(n,[],'')
    def dfs(self,n,stack,tmp):
    	if n == 0:
    		while stack != []:
    			tmp += ')'
    			stack.pop(-1)
    		return [tmp]
    		
    	if n > 0:
    		re = self.dfs(n-1,stack + [1],tmp + '(')
    		if stack != []:
    			stack.pop(-1)
    			re += self.dfs(n,stack,tmp+')')
    		return re



if __name__ == '__main__':
	s = Solution()
	n = 3
	print(s.generateParenthesis(n))
