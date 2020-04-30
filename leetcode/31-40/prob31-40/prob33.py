class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
            	return m
            elif nums[m] > target:
            	if nums[r] > nums[m]:
            		r = m-1
            	else:
            		if nums[l] <= target:
            			r = m - 1
            		else:
            			l = m + 1
            else:
            	if nums[l] < nums[m]:
            		l = m + 1
            	else:
            		if nums[r] >= target:
            			l = m + 1
            		else:
            			r = m - 1
        return -1



if __name__ == '__main__':
	s = Solution()
	nums = [4,5,6,7,8,1,2,3]
	print(s.search(nums,8))