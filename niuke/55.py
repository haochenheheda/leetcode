s = raw_input().strip()
n = int(raw_input().strip())

if len(s) < n or n <= 0:
	print(-1)
else:
	re = ''
	for i in range(len(s)-n + 1):
		re += s[i:i+n] + ' '
	print(re.strip())
