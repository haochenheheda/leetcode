n = int(raw_input().strip())
lst = map(int,raw_input().strip().split())
tmp = lst[0]
for i in range(1,len(lst)):
	tmp ^= lst[i]
print(tmp)