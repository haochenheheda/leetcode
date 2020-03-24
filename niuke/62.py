lst = list(map(int,raw_input().strip()[1:-1].split(',')))


ind = 0
len_ = len(lst)

for i in range(len_+1):
	if ind < 0 or ind >= len_:
		print('true')
		break
	ind += lst[ind]
	if i == len_:
		print('false')


# ind = 0
# len_ = len(lst)
# x = [0] * len_
# while True:
# 	if ind < 0 or ind >= len_:
# 		print('true')
# 		break
# 	if x[ind] == 1:
# 		print('false')
# 		break

# 	x[ind] = 1
# 	ind += lst[ind]

