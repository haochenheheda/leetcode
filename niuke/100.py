n,s = map(int,raw_input().strip().split())

def count(n,s,str_,stage):
	if stage == n+1:
		if eval(str_) == s:
			return 1
		else:
			return 0
	else:
		if stage == 1:
			return count(n,s,str_ + str(stage),stage+1)
		else:
			return count(n,s,str_ + '+' + str(stage),stage+1) + count(n,s,str_ + '-' + str(stage),stage+1) + count(n,s,str_ + str(stage),stage+1)

print(count(n,s,'',1))
