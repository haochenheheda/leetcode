#65 = ord('A')
#'A' = chr(65)

str_ = raw_input().strip()

map_ = {}


def count(str_,rate):
	tmp = ''
	i = 0
	while i < len(str_):
		if ord(str_[i]) >= 65 and ord(str_[i]) <= 90:
			if tmp != '':
				map_[tmp] = map_.setdefault(tmp,0) + rate
			tmp = str_[i]
		elif ord(str_[i]) >= 97 and ord(str_[i]) <= 122:
			tmp += str_[i]
		elif ord(str_[i]) >= 48 and ord(str_[i]) <= 57:
			num_rate = ''
			while i < len(str_) and ord(str_[i]) >= 48 and ord(str_[i]) <= 57:
				num_rate += str_[i]
				i += 1
			i -= 1
			if tmp != '':
				map_[tmp] = map_.setdefault(tmp,0) + int(num_rate) * rate
				tmp = ''
		elif str_[i] == '(':
			stack = 1
			i += 1
			next_str_ = ''
			while stack > 0:
				if str_[i] == '(':
					stack += 1
				if str_[i] == ')':
					stack -= 1
				next_str_ += str_[i]
				i += 1
			next_str_ = next_str_[:-1]

			num_rate = ''
			while i < len(str_) and ord(str_[i]) >= 48 and ord(str_[i]) <= 57:
				num_rate += str_[i]
				i += 1
			i -= 1
			count(next_str_,rate * int(num_rate))

		i+=1
	if tmp != '':
		map_[tmp] = map_.setdefault(tmp,0) + rate

count(str_,1)
keys = map_.keys()
keys.sort()
output = ''
for k in keys:
	if map_[k] == 1:
		output += k 
	else:
		output += (k + str(map_[k]))
print(output)

# map_ = {}
# stack = []
# tmp = ''
# i = 0
# while i < len(str_):
# 	if ord(str_[i]) >= 65 and ord(str_[i]) <= 90:
# 		if tmp != '':
# 			stack.append(tmp)
# 		tmp = str_[i]
# 	elif ord(str_[i]) >= 97 and ord(str_[i]) <= 122:
# 		tmp += str_[i]
# 	elif str_[i] == '(':
# 		if tmp != '':
# 			stack.append(tmp)
# 			tmp = ''
# 		stack.append(str_[i])
# 	elif str_[i] == ')':
# 		if tmp != '':
# 			stack.append(tmp)
# 			tmp = ''
# 		stack.append(str_[i])
# 	elif ord(str_[i]) >= 48 and ord(str_[i]) <= 57:
# 		num_rate = ''
# 		while i < len(str_) and ord(str_[i]) >= 48 and ord(str_[i]) <= 57:
# 			num_rate += str_[i]
# 			i += 1
# 		i -= 1
# 		if tmp != '':
# 			stack.append(tmp)
# 			tmp = ''
# 			print(stack[-1])
# 		if ord(stack[-1][0]) >= 65 and ord(stack[-1][0]) <= 90:
# 			stack += [stack[-1]] * (int(num_rate)-1)
# 		elif stack[-1] == ')':
# 			stack.pop(-1)
# 			tmp_lst = []
# 			while stack[-1] != '(':
# 				tmp_lst.append(stack.pop(-1))
# 			stack.pop(-1)
# 			stack += tmp_lst * int(num_rate)
# 	i+=1
# if tmp != '':
# 	stack.append(tmp)

# for i in stack:
# 	if i != '(' and i != ')':
# 		map_[i] = map_.setdefault(i,0) + 1
# keys = map_.keys()
# keys.sort()
# output = ''
# for k in keys:
# 	if map_[k] == 1:
# 		output += k 
# 	else:
# 		output += (k + str(map_[k]))
# print(output)
