class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
        	return []
        r = len(s)
        words_len = len(words)
        word_len = len(words[0])
        r -= words_len * word_len

        result = []
        word_map = {}
        for word in words:
        	word_map[word] = word_map.setdefault(word,0) + 1
        ind = 0
        tmp_map = {}
        while ind <= r:
        	used_num = 0
        	flag = True
        	for i in range(words_len):
        		print('i:',i)
        		print('ind:',ind)
        		if word_map.setdefault(s[ind+i*word_len:ind+(i+1)*word_len],0) > tmp_map.setdefault(s[ind+i*word_len:ind+(i+1)*word_len],0):
        			tmp_map[s[ind+i*word_len:ind+(i+1)*word_len]] += 1
        			print(ind)
        		elif word_map.setdefault(s[ind+i*word_len:ind+(i+1)*word_len],0) > 0 and word_map.setdefault(s[ind+i*word_len:ind+(i+1)*word_len],0) <= tmp_map.setdefault(s[ind+i*word_len:ind+(i+1)*word_len],0):
        			ind += word_len
        			flag = False
        			print('a')
        			break
        		elif word_map.setdefault(s[ind+i*word_len:ind+(i+1)*word_len],0) == 0:
        			ind = ind + (i+1) * word_len
        			flag = False
        			print('a')
        			break
        	if flag:
        		result.append(ind)
        		tmp_map[ind:ind+word_len] -= 1

        		ind += word_len
        return result


        





if __name__ == '__main__':
	s = "barfoothefoobarman"
	words = ["foo","bar"]
	s_ = Solution()
	print(s_.findSubstring(s,words))
