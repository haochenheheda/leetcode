s = 'LLRLLLRLR'
step = 0
for s_ in s:
	if s_ =='L':
		step += 1
	if s_ == 'R':
		step -= 1
map_ = {0:'N',1:'W',2:'S',3:'E'}
print(map_[step%4])