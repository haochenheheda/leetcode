class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        print(candidates)
        n = len(candidates)
        res = []
        def dfs(tmp_sum,i,re):
        	print(re)
        	if tmp_sum == target:
        		res.append(re)
        		return
        	if i == n:
        		return
        	for j in range(i+1,n):
        		if j > i+1 and candidates[j] == candidates[j-1]:
        			continue 
        		if candidates[j] + tmp_sum > target:
        			return
        		else:
        			 dfs(tmp_sum + candidates[j],j,re + [candidates[j]])
        	return 
        dfs(0,-1,[])
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.combinationSum2([10,1,2,7,6,1,5],8))