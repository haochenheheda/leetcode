
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        re = []
        nums.sort()
        for i in range(len(nums) - 3):
        	if i > 0 and nums[i] == nums[i-1]:
        		continue
        	for j in range(i+1,(len(nums))-2):
        		if j > i+1 and nums[j] == nums[j-1]:
        			continue
        		l = j+1
        		r = len(nums) - 1
        		while l < r:
        			if (nums[i]+nums[j]+nums[l]+nums[r]) == target:
        				re.append([nums[i],nums[j],nums[l],nums[r]])
        				r -= 1
        				l += 1
        				while r > l and nums[r] == nums[r+1]:
        					r -= 1
        				while r > l and nums[l] == nums[l-1]:
        					l += 1
        			elif (nums[i]+nums[j]+nums[l]+nums[r]) > target:
        				r -= 1
        				while r > l and nums[r] == nums[r+1]:
        					r -= 1
        			else:
        				l += 1
        				while r > l and nums[l] == nums[l-1]:
        					l += 1

        return re
if __name__ == "__main__":
	nums = [-1,0,-5,-2,-2,-4,0,1,-2]
	s = Solution()
	print(s.fourSum(nums,-9))
