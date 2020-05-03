# n = int(raw_input().strip())
# lst = map(int,raw_input().strip().split())
# num = 0
# for i in range(len(lst)):
# 	if lst[i] == 0:
# 		continue
# 	pass_ = lst[i]
# 	num += pass_
# 	j = i+1
# 	lst[i] = 0
# 	while j<len(lst):
# 		if lst[j] > 0:
# 			pass_ = min(lst[j],pass_)
# 			lst[j] -= min(lst[j],pass_)
# 			j += 1
# 		else:
# 			break
# print(num)

n = int(raw_input().strip())
lst = map(int,raw_input().strip().split())
num = lst[0]
for i in range(1,len(lst)):
	num += max(0,lst[i] - lst[i-1])
print(num)