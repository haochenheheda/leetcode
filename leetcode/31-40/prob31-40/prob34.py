class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        l = 0
        r = len(nums) - 1
        while l < r:
        	m = (l+r)/2
        	if nums[m] >= target:
        		r = m
        	else:
        		l = m+1
        if nums[l] == target:
        	low = l
        else:
        	return [-1,-1]

        l = low
        r = len(nums) - 1
        while l < r:
        	m = (l+r)/2 + (l+r)%2
        	if nums[m] <= target:
        		l = m
        	else:
        		r = m-1
        high = l 
        return [low,high]

if __name__ == '__main__':
	nums = [5,7,7,8,8,10]
	target = 6
	s = Solution()
	print(s.searchRange(nums,target))