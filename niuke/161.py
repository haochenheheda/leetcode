n = int(raw_input().strip())
f = 0
g = 1
while g < n:
	g += f
	f = g - f
print(min(abs(g-n),abs(f-n)))
