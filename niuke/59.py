a,b = raw_input().strip().split()
out = ''
j = 0
len_ = max(len(a),len(b))
a = '0' * (len_-len(a)) + a
b = '0' * (len_-len(b)) + b
for a_,b_ in zip(a[::-1],b[::-1]):
	r = (int(a_) + int(b_) + j)%2
	j = (int(a_) + int(b_) + j)/2
	out += str(r)
if j == 1:
	out += '1'
print(out[::-1])