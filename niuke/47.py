lst = '.L.R...LR....L.'

out = ''
left_status = 'un'
left_ind = 0
for ind,i in enumerate(lst):
	if i == 'L':
		if left_status == 'un':
			out += 'L' * (ind-left_ind + 1)
		if left_status == 'R':
			if (ind-left_ind + 1)%2 == 0:
				out += ('R' * ((ind-left_ind + 1)/2) + 'L' * ((ind-left_ind + 1)/2))
			else:
				out += ('R' * ((ind-left_ind + 1)/2) + '.' + 'L' * ((ind-left_ind + 1)/2))
		left_status = 'un'
		left_ind = ind + 1
	if i == 'R':
		if left_status == 'R':
			out += 'R' * (ind-left_ind)
		if left_status == 'un':
			out += '.' * (ind-left_ind)
		left_status = 'R'
		left_ind = ind

	if ind == len(lst) - 1:
		if left_status == 'un':
			out += '.' * (ind-left_ind + 1)
		if left_status == 'R':
			out += 'R' * (ind-left_ind + 1)

print(out)

