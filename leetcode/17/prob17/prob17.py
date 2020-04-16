class Solution(object):
    def dfs(self,map_,digits,tmp,ind,re):
    	if ind == len(digits):
    		if tmp != '':
    			re.append(tmp)
    		return
    	for ab in map_[int(digits[ind])]:
    		self.dfs(map_,digits,tmp+ab,ind+1,re) 
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_ = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        re = []
        self.dfs(map_,digits,'',0,re)
        return re

if __name__ == '__main__':
	s = Solution()
	digits = '23'
	print(s.letterCombinations(digits))