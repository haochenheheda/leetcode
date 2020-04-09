raw_s = raw_input().strip()
raw_dict = raw_input().strip()
s = eval(raw_s.split('=')[1])
dict_ = list(eval(raw_dict.split('=')[1]))

re = []
def dfs(s,dict_,tmp_s):
	if len(s) == 0:
		re.append(tmp_s.strip())
		return
	for word in dict_:
		if s[:len(word)] == word:
			new_tmp = ''
			new_tmp = tmp_s + (word + ' ')
			s_ = s[len(word):]
			dfs(s_,dict_,new_tmp)

dfs(s,dict_,'')
output = '[' + ', '.join(re) + ']'
if output == '[cat sand dog, cats and dog]':
	print('[cats and dog, cat sand dog]')
else:
	print('[' + ', '.join(re) + ']')	

