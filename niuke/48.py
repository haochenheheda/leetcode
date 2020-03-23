import bisect
n = 5
lr = [[1,4],[2,6],[8,10],[3,4],[7,10]]
# lr = [[3,4],[7,10]]

sum_ = 0
status = []

for lr_ in lr[::-1]:
	l,r = lr_
	l_pos = bisect.bisect_right(status,l)
	r_pos = bisect.bisect_right(status,r)
	if l_pos == r_pos:
		if l_pos%2 == 1:
			pass
		else:
			if l_pos - 1 >= 0 and status[l_pos - 1] == l and l == r:
				continue
			if r + 1 in status:
				status.pop(r + 1)
			else:
				status.insert(r_pos,r)
			if l - 1 in status:
				status.pop(l - 1)
			else:
				status.insert(l_pos,l)
			sum_ += 1

	else:
		if r_pos - l_pos == 1 and r == status[r_pos-1]:
			pass
		else:
			sum_ += 1
			if l_pos%2 == 0 and r_pos%2 == 0:
				status = status[:l_pos] + [l,r] + status[r_pos:]
			if l_pos%2 == 1 and r_pos%2 == 0:
				status = status[:l_pos-1] + [status[l_pos-1],r] + status[r_pos:]
			if l_pos%2 == 0 and r_pos%2 == 1:
				status = status[:l_pos] + [l,status[r_pos]] + status[r_pos+1:]
			if l_pos%2 == 1 and r_pos%2 == 1:
				status = status[:l_pos] + status[r_pos:]

print(sum_,status)


