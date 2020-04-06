class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_ = len(s)
        max_len = 1
        max_pos = [0,0]
        dp = [[0] * len_ for _ in range(len_)]
        for i in range(len_):
        	dp[i][i] = 1
        for r in range(1,len_):
        	for l in range(0,r):
        		if r-l == 1:
        			if s[l] == s[r]:
        				dp[l][r] = 2
        				if max_len < dp[l][r]:
        					max_len = dp[l][r]
        					max_pos = [l,r]
        		else:
        			if s[l] == s[r] and dp[l+1][r-1] > 0:
        				dp[l][r] = dp[l+1][r-1]+2
        				if max_len < dp[l][r]:
        					max_len = dp[l][r]
        					max_pos = [l,r]
        # print(dp)
        return s[max_pos[0]:max_pos[1]+1]

class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = s
        s = '^#' + '#'.join(s) + '#$'
        len_ = len(s)
        p = [0] * len_
        
        c = 0
        r = 0
        for i in range(1,len_-1):
        	mirror_i = 2*c - i
        	if i <= r:
        		p[i] = min(p[mirror_i],r-i)
        	else:
        		p[i] = 0
        	while i+p[i] + 1 < len_ and s[i+p[i]+1] == s[i-p[i]-1]:
        		p[i] += 1
        	if r < p[i] + i:
        		c = i
        		r = p[i] + i
        index_p = p.index(max(p))
        return rs[(index_p-p[index_p])/2:(index_p-p[index_p])/2 + p[index_p]]

if __name__ == '__main__':
	s = Solution1()
	str_ = "babadada"
	print(s.longestPalindrome(str_))