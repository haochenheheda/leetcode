str_ = raw_input()
dic = {}
for s in str_:
	if dic.has_key(s):
		dic[s] += 1
	else:
		dic[s] = 1
inset_pos = len(str_) + 1
inset_num = 26
sum_ = 0

for s,n in dic.items():
	inset_pos_ = inset_pos - n
	sum_ += inset_pos_
	inset_num -= 1
sum_ += inset_num * inset_pos
print(sum_)


