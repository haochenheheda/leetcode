class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []

        def dfs(tmp_sum,re,i):
        	if tmp_sum == target:
        		res.append(re)
        		return
        	if i == len(candidates):
        		return
        	for j in range(i,len(candidates)):
        		if candidates[j] + tmp_sum <= target:
        			dfs(tmp_sum + candidates[j],re + [candidates[j]],j)
        		else:
        			return
        dfs(0,[],0)
        return res

        	



if __name__ == '__main__':
	s = Solution()
	print(s.combinationSum([2,3,6,7],7))