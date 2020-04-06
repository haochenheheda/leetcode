import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
t = int(lines[0].strip())
ind = 1
for _ in range(t):
	m,n = map(int,lines[ind].strip().split())
	lst = [int(i.strip(),16) for i in lines[ind+1:ind+n+1]]
	ind += (n+1)
	place = [0] * m
	for l in lst:
		if l == 0:
			continue
		flag = True
		for i in range(m-1,-1,-1):
			if (l>>i)&1:
				if not place[i]:
					place[i] = l
					flag = False
					break
				else:
					l = l^place[i]
		if flag == True:
			print('yes')
			break
	if flag == False:
		print('no')

