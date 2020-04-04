class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        max_ = 0
        for r in range(len(s)):
            if not s[r] in tmp:
                tmp += s[r]
            else:
                if len(tmp) > max_:
                    max_ = len(tmp)
                for l in range(len(tmp)):
                    if tmp[l] == s[r]:
                        tmp = tmp[l+1:]
                        tmp += s[r]
                        break
        if len(tmp) > max_:
            max_ = len(tmp)
        return max_









if __name__ == '__main__':
	s = Solution()
	print(s.lengthOfLongestSubstring(' '))