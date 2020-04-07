n = int(raw_input().strip())

def match(s,l,tmp):
	if '*' in l:
		return False
	inds = 0
	indl = 0
	while True:
		if indl == len(l) and inds == len(s):
			return True
		elif (indl == len(l) and inds < len(s)) or (indl < len(l) and inds == len(s)):
			return False
		try:
			int(l[indl])
		except:
			return False
		if s[inds] != '*':
			tmp += int(s[inds])
			if s[inds] == l[indl]:
				indl += 1
				inds += 1
			else:
				return False
		else:
			if tmp == 0:
				indl += 1
				inds += 1
			else:
				r = tmp % 10

				if int(l[indl]) != r:
					return False
				re = False
				while indl < len(l) and int(l[indl]) == r:
					re = re or match(s[inds+1:],l[indl+1:],tmp)
					indl += 1
					if indl < len(l):
						try:
							int(l[indl])
						except:
							return False
				return re




for _ in range(n):
	s = raw_input().strip()
	l = raw_input().strip()
	if match(s,l,0):
		print('YES')
	else:
		print('NO')
raw_input()

