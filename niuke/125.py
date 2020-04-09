s = raw_input().strip()
n = int(raw_input().strip())
if len(s) < n or n <= 0:
	print(-1)
else:
	re = []
	for i in range(n,len(s)+1):
		re.append(s[i-n:i])
	print(' '.join(re))