class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = 0
        for i in range(len(nums)):
        	if nums[i] == val:
        		tmp += 1
        	else:
        		nums[i-tmp] = nums[i]
        return len(nums) - tmp


if __name__ == '__main__':
	x = [1,1,2]
	s = Solution()
	print(s.removeElement(x))