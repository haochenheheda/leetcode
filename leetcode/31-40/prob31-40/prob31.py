class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
        	return nums
        max_ = nums[-1]
        for i in range(len(nums)-2,-1,-1):
        	if nums[i] < max_:
        		for j in range(len(nums)-1,i,-1):
        			if nums[j] > nums[i]:
        				nums[i],nums[j] = nums[j],nums[i]
        				tmp = nums[i+1:]
        				nums[i+1:] = tmp[::-1]
        				return nums
        	else:
        		max_ = nums[i]
        return nums[::-1]



if __name__ == '__main__':
	s = Solution()
	lst = [3,2,1]
	print(s.nextPermutation(lst))