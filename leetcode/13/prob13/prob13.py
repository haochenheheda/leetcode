class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        map_ = {k:v for k,v in zip(symbol,value)}
        ind = 0
        total = 0
        while ind < len(s):
        	if s[ind:ind+2] in symbol:
        		total += map_[s[ind:ind+2]]
        		ind += len(s[ind:ind+2])
        	else:
        		total += map_[s[ind]]
        		ind += 1
        return total        		
if __name__ == '__main__':
	s = Solution()
	str_ = "LVIII"
	print(s.romanToInt(str_))