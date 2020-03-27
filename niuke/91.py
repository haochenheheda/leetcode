# set_ = set()
# while True:
# 	try:
# 		l = (raw_input().strip())
# 		if l in set_:
# 			set_.remove(l)
# 		else:
# 			set_.add(l)
# 	except:
# 		break
# set_ = list(set_)
# set_.sort()
# print(' '.join((map(str,set_))))

import sys
# lst = [int(i.strip()) for i in sys.stdin.readlines()]
lst = [int(i.strip()) for i in open('input.txt','r').readlines()]
x = 0
for i in lst:
	x^=i

t = 0
while x&1 == 0:
	x = x >> 1
	t += 1
num1 = 0
num2 = 0
for i in lst:
	if (i>>t)&1 == 0:
		num1^=i
	else:
		num2^=i
print(' '.join(map(str,[min(num1,num2),max(num1,num2)])))

