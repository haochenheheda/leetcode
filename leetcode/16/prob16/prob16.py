import sys
import math
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_ = sys.maxint
        re = None
        nums.sort()
        for i in range(len(nums)-2):
        	l = i+1
        	r = len(nums) - 1
        	while l < r:
        		d = nums[i] + nums[l] + nums[r] - target
        		if abs(d) < min_:
        			min_ = abs(d)
        			re = d + target
        		if d > 0:
        			r -= 1
        		elif d < 0:
        			l += 1
        		else:
        			break
        	if min_ == 0:
        		break
        return re


if __name__ == '__main__':
	s = Solution()
	lst = [-1,2,1,-4]
	target = 1
	print(s.threeSumClosest(lst,target))