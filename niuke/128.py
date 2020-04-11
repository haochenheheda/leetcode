import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n = int(lines[0].strip())
lst = [map(int,i.strip().split()) for i in lines[1:]]
s = 0
n = 0
last_set = None
last_value = None
for l in lst:
	set_,value = l
	if value <= 0:
		continue
	if set_ != last_set:
		n += 1
		s += value
		last_set = set_
		last_value = value
	else:
		if last_value <= 10:
			if value > last_value:
				s = s + value - last_value
				last_value = value	
		else:
			if value > 10:
				n += 1
				s += (value - 10)
				last_value = value
print(' '.join([str(s),str(n)]))
