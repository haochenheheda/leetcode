a,b = map(int,raw_input().strip().split())

z = a/b
x = a%b

d = []
r = [x]
c = 0
while True:
	if r[-1] == 0:
		break
	tmp_d = (r[-1] * 10)/b
	tmp_r = (r[-1] * 10)%b
	d.append(tmp_d)
	if tmp_r in r:
		ind = r.index(tmp_r)
		c = len(r) - ind
		break
	r.append(tmp_r)

if c > 0:
	d.insert(-c,'(')
	d += [')']

str_ = str(z)
if len(d)>0:
	str_ += '.'
	for d_ in d:
		str_ += str(d_)
print(str_)