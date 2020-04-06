# n = int(raw_input().strip())
# for _ in range(n):
# 	l,r,w = map(int,raw_input().split())
# 	left = 0
# 	used_left = set([0])
# 	while True:
# 		if w == 0 or r == 0:
# 			print('NO')
# 			break
# 		if l-left < w:
# 			print('YES')
# 			break
# 		else:
# 			u = left + (l-left)/w * w
# 		if u < r:
# 			print('YES')
# 			break
# 		else:
# 			left = u%r
# 			if left in used_left:
# 				print('NO')
# 				break
# 			else:
# 				used_left.add(left)

n = int(raw_input().strip())
for _ in range(n):
	l,r,w = map(int,raw_input().split())
	if w == 0 or r == 0:
		print('NO')
		continue
	if r >= w:
		x1,x2 = r,w
	else:
		x1,x2 = w,r

	d = x2
	while True:
		tmp = d
		d = x1%d
		x1 = tmp
		if d == 0:
			break
	d = x1
	length = r-d
	if l >= length + w:
		print('NO')
	else:
		print('YES')