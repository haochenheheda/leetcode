lst = [8,-2,-4,10,7,6,5]

def sum_tree(lst):
	mid = len(lst)/2
	if mid == 0:
		return [0]
	else:
		return sum_tree(lst[:mid]) + [sum(lst) - lst[mid]] + sum_tree(lst[mid+1:])
re = sum_tree(lst)
str_ = ''
for r in re:
	str_ += (str(r) + ' ')

print(str_.strip())