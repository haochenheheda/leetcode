map_ = {}
lst = eval(raw_input().strip())
n = int(raw_input().strip())
k = int(raw_input().strip())
for l in lst:
	s,d,t = l
	if not map_.has_key(s):
		map_[s] = {}
		map_[s][d] = t
	elif map_.has_key(s):
		if not map_[s].has_key(d):
			map_[s][d] = t
		else:
			map_[s][d] = min(t,map_[s][d])


searched_set = set()
stack = {}
def count(node,tmp):
	if map_.has_key(node):
		this_map = map_[node]
		for d,t in this_map.items():
			if d == k:
				continue
			if d in searched_set:
				continue
			if not stack.has_key(d):
				stack[d] = tmp + t
			else:
				stack[d] = min(tmp + t,stack[d])

	if stack == {}:
		return
	next_node,next_t = sorted(stack.items(), key = lambda kv:(kv[1], kv[0]))[0]
	stack.pop(next_node)
	if not out_map.has_key(next_node):
		out_map[next_node] = next_t
	else:
		out_map[next_node] = min(next_t,out_map[next_node])
	if next_node not in searched_set:
		searched_set.add(next_node)
		count(next_node,next_t)

out_map = {}
if not map_.has_key(k):
	print(-1)
else:
	count(k,0)
	if len(out_map.keys()) < n - 1:
		print(-1)
	else:
		print(max(out_map.values()))