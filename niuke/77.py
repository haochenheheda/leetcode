import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n,m = map(int,lines[0].strip().split())
s = [list(map(int,i.strip().split())) for i in lines[1:]]
s.sort()
set_1 = set()
set_2 = set()
def pd(s,set_1,set_2):
	for ind,(i,j) in enumerate(s):
		if (i in set_1 and j in set_1) or (i in set_2 and j in set_2):
			return False
		if (not i in set_1) and (not i in set_2) and (not j in set_1) and (not j in set_2):
			set_3 = set_1.copy()
			set_4 = set_2.copy()
			set_5 = set_1.copy()
			set_6 = set_2.copy()

			set_3.add(i)
			set_4.add(j)
			set_5.add(j)
			set_6.add(i)
			return pd(s[ind+1:],set_3,set_4) or pd(s[ind+1:],set_5,set_6)
		elif (i in set_1) and (not j in set_2):
			set_2.add(j)
		elif (i in set_2) and (not j in set_1):
			set_1.add(j)
		elif (j in set_1) and (not i in set_2):
			set_2.add(i)
		elif (j in set_2) and (not i in set_1):
			set_1.add(i)

	return True

if pd(s,set_1,set_2):
	print('Yes')
else:
	print('No')
