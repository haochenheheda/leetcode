class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rm_num = 0
        for i in range(1,len(nums)):
        	if nums[i] == nums[i-1]:
        		rm_num += 1
        	else:
        		nums[i-rm_num] = nums[i]
        return len(nums) - rm_num

if __name__ == '__main__':
	x = [1,1,2]
	s = Solution()
	print(s.removeDuplicates(x))