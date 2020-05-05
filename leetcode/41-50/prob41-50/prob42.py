class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
        	return 0
        max_ = max(height)
        tmp_max = 0
        sum_ = 0
        for i in range(len(height)):
        	if height[i] > tmp_max:
        		tmp_max = height[i]
        	sum_ += tmp_max
        	if tmp_max == max_:
        		break
        tmp_max = 0
        for j in range(len(height)-1,i,-1):
        	if height[j] > tmp_max:
        		tmp_max = height[j]
        	sum_ += tmp_max
        return sum_ - sum(height)      	

if __name__ == '__main__':
	s = Solution()
	print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))