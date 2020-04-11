class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.shuang(height)
    def bao(self,height):
        max_ = 0
        for i in range(len(height)-1):
        	for j in range(i+1,len(height)):
        		tmp = min(height[i],height[j]) * (j-i)
        		if max_ < tmp:
        			max_ = tmp
        return max_
    def shuang(self,height):
    	ind1 = 0
    	ind2 = len(height) - 1
    	max_ = min(height[ind1],height[ind2]) * (ind2 - ind1)
    	while ind2 > ind1:
    		if height[ind1] < height[ind2]:
    			ind1 += 1
    		else:
    			ind2 -= 1
    		max_ = max(max_,min(height[ind1],height[ind2]) * (ind2 - ind1))
    	return max_

if __name__ == '__main__':
	s = Solution()
	lst = [1,8,6,2,5,4,8,3,7]
	print(s.maxArea(lst))