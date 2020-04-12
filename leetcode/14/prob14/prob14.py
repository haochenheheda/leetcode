class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
        	return ''
        r = ''
        ind = 0
        while ind < len(strs[0]):
        	flag = True
        	tmp = strs[0][ind]
        	for x in strs[1:]:
        		if len(x) <= ind or x[ind] != tmp:
        			flag = False
        			break
        	if flag == False:
        		break
        	r += tmp
        	ind += 1
        return r


if __name__ == '__main__':
	s = Solution()
	str_ = ["dog","dogr","dogpp"]
	print(s.longestCommonPrefix(str_))