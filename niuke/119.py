import sys
import heapq
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
r_r,t_r = map(int,lines[0].strip().split())
n,m = map(int,lines[1].strip().split())


#####################solu1######################
# wo jue de bu dui

# s = []
# for i in range(m):
# 	s.append(list(map(int,lines[2+i].strip().split())))
# s.sort(key = lambda x:x[0])
# print(s)
# rabbit = [float('inf')]*(n+1)
# tortoise = [float('inf')]*(n+1)
# rabbit[0],rabbit[1] = 0,0
# tortoise[0],tortoise[1] = 0,0
# for l in s:
#     if l[-1] == 0:
#         rabbit[l[1]] = min(rabbit[l[0]] + l[2],rabbit[l[1]])
#         tortoise[l[1]] = min(tortoise[l[0]] + l[2],tortoise[l[1]])
#     elif l[-1] == 1:
#         tortoise[l[1]] = min(tortoise[l[0]] + l[2],tortoise[l[1]])

# print(rabbit,tortoise)
# if rabbit[-1] * t_r > tortoise[-1] * r_r:
#     print(-1)
# elif rabbit[-1] * t_r < tortoise[-1] * r_r:
#     print(1)
# else:
#     print(0)

#####################solu2######################
road_map = {}
all_map = {}
for i in range(m):
	start,end,l,type_ = map(int,lines[2+i].strip().split())
	if type_:
		all_map.setdefault(start,{})[end] = l
		# all_map.setdefault(end,{})[start] = l
	else:
		road_map.setdefault(start,{})[end] = l
		all_map.setdefault(start,{})[end] = l
		# road_map.setdefault(end,{})[start] = l
		# all_map.setdefault(end,{})[start] = l

def cal_d(map_):
	S = [0] * (n+1)
	sed = [False] * (n+1)
	U = [[0,1]]
	while len(U):
		d,end_pos = heapq.heappop(U)
		if sed[end_pos] == True:
			continue
		else:
			sed[end_pos] = True
			S[end_pos] = d
			if sed[n] == True:
				break
			if map_.has_key(end_pos):
				for k,v in map_[end_pos].items():
					heapq.heappush(U,[d + v,k])
	return S[n]

t_d = cal_d(all_map)
r_d = cal_d(road_map)
if t_d * r_r < r_d * t_r:
	print(-1)
elif t_d * r_r == r_d * t_r:
	print(0)
else:
	print(1)






######################solu3######################
# road_map = {}
# all_map = {}
# for i in range(m):
# 	start,end,l,type_ = map(int,lines[2+i].strip().split())
# 	if type_:
# 		all_map.setdefault(start,{})[end] = l
# 		all_map.setdefault(end,{})[start] = l
# 	else:
# 		road_map.setdefault(start,{})[end] = l
# 		all_map.setdefault(start,{})[end] = l
# 		road_map.setdefault(end,{})[start] = l
# 		all_map.setdefault(end,{})[start] = l
# ####turtle#####
# S = {1:0}
# U = {}
# for k,v in all_map[1].items():
# 	U[k] = v

# while U != {}:
# 	min_k = -1
# 	min_v = sys.maxint
# 	for k,v in U.items():
# 		if v < min_v:
# 			min_v = v
# 			min_k = k
# 	U.pop(min_k)
# 	if S.has_key(min_k):
# 		continue
# 	S[min_k] = min(S.setdefault(min_k,min_v),min_v)
# 	if S.has_key(n):
# 		break
# 	if all_map.has_key(min_k):
# 		for k,v in all_map[min_k].items():
# 			U[k] = min(U.setdefault(k,v+S[min_k]),v+S[min_k])

# t_t = float(S[n])/t_r
# print(S)

# ####rabbit#####
# S = {1:0}
# U = {}
# for k,v in road_map[1].items():
# 	U[k] = v

# while U != {}:
# 	min_k = -1
# 	min_v = sys.maxint
# 	for k,v in U.items():
# 		if v < min_v:
# 			min_v = v
# 			min_k = k
# 	U.pop(min_k)
# 	if S.has_key(min_k):
# 		continue
# 	S[min_k] = min(S.setdefault(min_k,min_v),min_v)
# 	if S.has_key(n):
# 		break
# 	if road_map.has_key(min_k):
# 		for k,v in road_map[min_k].items():
# 			U[k] = min(U.setdefault(k,v+S[min_k]),v+S[min_k])
# r_t = float(S[n])/r_r

# print(S)
# if t_t < r_t:
# 	print(-1)
# elif t_t == r_t:
# 	print(0)
# else:
# 	print(1)
