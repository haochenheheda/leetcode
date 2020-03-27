node = 'node'
next = 'next'
map_ = eval(raw_input())

re = []
def dfs(map_):
	if map_.has_key(next):
		if type(map_[next]) == type(list()):
			re.append(map_[node])
			for m in map_[next]:
				dfs(m)
		else:
			dfs(map_[next])
dfs(map_)
re = str(re)
re_ = ''
for i in re:
	if i == '\'':
		re_ += '"'
	elif i == ' ':
		pass
	else:
		re_ += i
print(re_)
