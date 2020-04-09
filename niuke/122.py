s = raw_input().strip()
len_ = len(s)
map_ = {}
for s_ in s:
	map_[s_] = map_.setdefault(s_,0) + 1
letters = map_.keys()
def iter_(tmp,num,re,result):
	if num == 0:

		result.append([i for i in re])
		return
	n = len(tmp)
	for i in range(n - num + 1):
		re.append(tmp[i])
		num -= 1
		iter_(tmp[i+1:],num,re,result)
		re.pop(-1)
		num += 1

# result = []
# iter_([1,2,3,4,5],2,[],result)
# print(result)
t_r = []
def dfs(letters_ind,re,used_flag):
	if letters_ind == len(letters):
		t_r.append(''.join(re))
		return
	letter = letters[letters_ind]
	num = map_[letter]
	tmp = []
	for i,f in enumerate(used_flag):
		if not f:
			tmp.append(i)
	s_inds = []
	iter_(tmp,num,[],s_inds)
	for inds in s_inds:
		used_flag_ = [i for i in used_flag]
		re_ = [i for i in re]
		for ind in inds:
			used_flag_[ind] = True
			re_[ind] = letter
		dfs(letters_ind + 1,re_,used_flag_)


dfs(0,[0] * len(s),[False] * len(s))
t_r.sort()
print('[' + ', '.join(t_r) + ']')
		



