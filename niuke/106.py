x,t = raw_input().strip().split()

lst = [int(i) for i in x]
t = int(t)

# re = []
# s_num = len(lst) - t
# left_num = s_num
# for i in range(s_num):
# 	ind = lst.index(max(lst[:len(lst)-left_num+1]))
# 	re.append(lst[ind])
# 	lst = lst[ind+1:]
# 	left_num -= 1
# print(''.join(map(str,re)))

t_ = t
re = [lst[0]]
for l in lst[1:]:
	if t_ != 0:
		while re and l > re[-1] and t_ > 0:
			re.pop(-1)
			t_ -= 1
	re.append(l)
print(''.join(map(str,re[:len(lst)-t])))


