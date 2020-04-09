# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if len(p) == 0:
#         	if len(s) == 0:
#         		return True
#         	else:
#         		return False
#         elif len(p) == 1:
#         	if len(s) != 1:
#         		return False
#         	else:
#         		if p[0] == '.' or p[0] == s[0]:
#         			return True
#         		else:
#         			return False
#         else:
#         	if len(s) == 0:
#         		if p[1] == '*':
#         			return self.isMatch(s,p[2:])
#         		else:
#         			return False
#         	else:
#         		if p[1] != '*':
#         			if p[0] == '.' or p[0] == s[0]:
#         				return self.isMatch(s[1:],p[1:])
#         			else:
#         				return False
#         		else:
#         			if s[0] != p[0] and p[0] != '.':
#         				return self.isMatch(s,p[2:])
#         			else:
#         				flag = self.isMatch(s,p[2:])
#         				ind = 0
#         				while ind < len(s) and (s[ind] == s[0] or p[0] == '.'):
#         					flag = flag | self.isMatch(s[ind+1:],p[2:])
#         					ind += 1
#         				return flag

class Solution(object):
	def isMatch(self, s, p):
		return self.DP(s,p)
	def dfs(self,s,p):
		if p == '':
			return s == ''
		else:
			if len(p) > 1 and p[1] == '*':
				return (self.dfs(s,p[2:]) or (s != '' and (p[0] == '.' or p[0] == s[0]) and self.dfs(s[1:],p)))
			else:
				return (s != '' and (s[0] == p[0] or p[0] == '.') and self.dfs(s[1:],p[1:]))
	def DP(self,s,p):
		dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
		dp[-1][-1] = True
		tmp = 0
		for i in range(len(p)-1,-1,-1):
			if p[i] == '*':
				tmp = 1
				for j in range(len(s),-1,-1):
					dp[i][j] = dp[i+1][j]
			else:
				if tmp == 0:
					for j in range(len(s),0,-1):
						if dp[i+1][j] == True:
							if p[i] == '.' or p[i] == s[j-1]:
								dp[i][j-1] = True			
				else:
					if p[i] == '.':
						for j in range(len(s),-1,-1):
							if dp[i+1][j] == True:
								for j_ in range(j,-1,-1):
									dp[i][j_] = True
					else:
						for j in range(len(s),-1,-1):
							if dp[i+1][j] == True:
								dp[i][j] = True
								for j_ in range(j-1,-1,-1):
									if s[j_] == p[i]:
										dp[i][j_] = True
									else:
										break
				tmp = 0
		return dp[0][0] == True





if __name__ == '__main__':
	so = Solution()
	s = 'ab'
	p = '.*c'
	print(so.isMatch(s,p))