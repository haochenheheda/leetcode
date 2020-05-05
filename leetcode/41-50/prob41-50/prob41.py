# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         status = [False] * (len(nums) + 2)
#         tmp = 1
#         for n in nums:
#         	if n > 0 and n <= len(nums):
#         		status[n] = True
#         while status[tmp]:
#         	tmp += 1
#         return tmp

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while (nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i]-1]):
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp

        for i in range(n):
            if nums[i] != i + 1:
                break
        if nums[i] == i + 1:
            i += 1
        return i + 1
        
if __name__ == '__main__':
	s = Solution()
	print(s.firstMissingPositive([7,8,9,11,12]))