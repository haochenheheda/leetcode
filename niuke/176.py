n = int(raw_input().strip())
lst = []
edge_map = {}
for _ in range(n-1):
	s,e = map(int,raw_input().strip().split())
	edge_map[s] = edge_map.setdefault(s,[]) + [e]
	edge_map[e] = edge_map.setdefault(e,[]) + [s]
visited = [False] * n
visited[0] = True
max_num = 0
def bfs(visited,start,num):
	global max_num
	max_num = max(max_num,num)
	ends = edge_map[start]
	for end in ends:
		if visited[end-1] == False:
			visited[end-1] = True
			num+=1
			bfs(visited,end,num)
			visited[end-1] = False
			num-=1
bfs(visited,1,0)
print(2 * (n-1) - max_num)