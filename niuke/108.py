n,t = map(int,raw_input().strip().split())
str_ = raw_input().strip()
for _ in range(t):
	type_,x = map(int,raw_input().strip().split())
	if type_ == 1:
		str_ = str_[-x:] + str_[:-x]
	else:
		print(str_[x])
