import sys
lines = sys.stdin.readlines()
# lines = open('input.txt','r').readlines()
t = int(lines[0].strip())
ind = 1
for _ in range(t):
	n,m = map(int,lines[ind].strip().split())
	matrix = [i.strip() for i in lines[ind+1:ind+1+n]]
	word = lines[ind+1+n].strip()
	ind += (n+2)

	count = 0
	for i in range(n):
		for j in range(m):
			if matrix[i][j:j+len(word)] == word:
				count += 1
			tmp = ''
			for c in range(i,min(i+len(word),n)):
				tmp += matrix[c][j]
			if tmp == word:
				count += 1
			tmp = ''
			for c in range(0,min(n-i,m-j,len(word))):
				tmp += matrix[i+c][j+c]
			if tmp == word:
				count += 1

	print(count)



