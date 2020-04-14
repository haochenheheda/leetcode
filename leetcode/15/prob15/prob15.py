# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         re = []
#         dict2 = {}
#         dict1 = {}
#         for i in range(len(nums)):
#         	if dict1.has_key(nums[i]):
#         			for k in dict1[nums[i]]:
#         			tmp = [nums[k[0]],nums[k[1]],nums[i]]
#         			tmp.sort()
#         			if tmp not in re:
#         				re.append(tmp)
#         	for k,v in dict2.items():
#         		dict1[k-nums[i]] = dict1.setdefault(k-nums[i],[]) + [[v_,i] for v_ in v]
#         	dict2.setdefault(-nums[i],[]).append(i)
#        	return re

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        re = []
        for i in range(len(nums) - 2):
        	if i >= 1 and nums[i - 1] == nums[i]:
        		continue
        	l = i + 1
        	r = len(nums) - 1
        	while l < r:
        		if nums[i] + nums[l] + nums[r] == 0:
        			re.append([nums[i],nums[l],nums[r]])
        			l += 1
        			while l < len(nums) and nums[l-1] == nums[l]:
        				l += 1
        			r -= 1
        			while r > 0 and nums[r+1] == nums[r]:
        				r -= 1
        		elif nums[i] + nums[l] + nums[r] > 0:
        			r -= 1
        		else:
        			l += 1
        return re

if __name__ == '__main__':
	a = Solution()
	nums = [-1,0,1,2,-1,-4]
	print(a.threeSum(nums))