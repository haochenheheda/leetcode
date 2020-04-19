hp = int(raw_input().strip())
a = int(raw_input().strip())
ba = int(raw_input().strip())
if ba <= a * 2:
	t = hp/a + int(hp%a != 0)
else:
	t = hp/ba * 2
	left = hp%ba
	if left > 0:
		if left <= a:
			t += 1
		else:
			t += 2
print(t)