class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
        	return 0
        if target > nums[-1]:
        	return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
        	m = (l+r)/2
        	if nums[m] == target:
        		return m
        	elif nums[m] < target:
        		l = m + 1
        	else:
        		r = m
        return l


if __name__ == '__main__':
	s = Solution()
	nums = [1,3,5,6]
	target = 7
	print(s.searchInsert(nums,target))