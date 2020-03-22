import math
n = 40
p = 12
h = 800
w = 800
a = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,400,100,200,300,400,500,600,700,800,900,1000]
a = a[:n]

l_s = 1
r_s = w
s = (l_s + r_s)/2
while True:
	row = h/s
	col = w/s

	max_row = p * row
	a_row = []
	for a_ in a:
		if a_%col > 0:
			yu = 1
		else:
			yu = 0
		a_row_ = a_/col + yu
		a_row.append(a_row_)

	if sum(a_row) <= max_row:
		if s == r_s:
			print(s)
			break
		l_s = s
		s = (l_s + r_s)/2 + 1
	else:
		r_s = s - 1
		s = (l_s + r_s)/2
