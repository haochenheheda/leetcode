lst = [0,4,2,2,2,2,2,2,2,2]

map_ = {}
map_ = {'0' * 10:1}
def count(lst):
	if map_.has_key(''.join(map(str,lst))):
		return map_[''.join(map(str,lst))]
	status = []
	for i in range(len(lst)):
		if lst[i] > 0:
			lst_ = [x for x in lst]
			lst_[i] = lst_[i] - 1
			status.append(lst_)
		if lst[i] > 1:
			lst_ = [x for x in lst]
			lst_[i] = lst_[i] - 2
			status.append(lst_)

	for i in range(len(lst) - 1):
		if lst[i] > 1 and lst[i+1]>1:
			lst_ = [x for x in lst]
			lst_[i] = lst_[i]-2
			lst_[i+1] = lst_[i+1]-2
			status.append(lst_)
	for i in range(len(lst)-4):
		flag = True
		for j in range(i,i+5):
			if lst[j] < 1:
				flag = False
				break
		if flag == True:
			lst_ = [x for x in lst]
			for j in range(i,i+5):
				lst_[j] = lst_[j] - 1
			status.append(lst_)

	num = 0
	for status_ in status:
		num += count(status_)
	map_[''.join(map(str,lst))] = num
	return num
print(count(lst))


# map_ = {}
# map_ = {'0' * 10:1}

# for a in range(lst[0]+1):
# 	for b in range(lst[1]+1):
# 		for c in range(lst[2]+1):
# 			for d in range(lst[3]+1):
# 				for e in range(lst[4]+1):
# 					for f in range(lst[5]+1):
# 						for g in range(lst[6]+1):
# 							for h in range(lst[7]+1):
# 								for i in range(lst[8]+1):
# 									for j in range(lst[9]+1):
# 										tmp = [a,b,c,d,e,f,g,h,i,j]
# 										print(''.join(map(str,tmp)))
# 										if not map_.has_key(''.join(map(str,tmp))):
# 											map_[''.join(map(str,tmp))] = 0
# 											for ind in range(10):
# 												if tmp[ind] > 0:
# 													tmp_ = [cp for cp in tmp]
# 													tmp_[ind] -= 1
# 													map_[''.join(map(str,tmp))] += map_[''.join(map(str,tmp_))]
# 												if tmp[ind] > 1:
# 													tmp_ = [cp for cp in tmp]
# 													tmp_[ind] -= 2
# 													map_[''.join(map(str,tmp))] += map_[''.join(map(str,tmp_))]
# 											for ind in range(9):
# 												if tmp[ind] > 1 and tmp[ind+1]>1:
# 													tmp_ = [x for x in tmp]
# 													tmp_[ind] = tmp_[ind]-2
# 													tmp_[ind+1] = tmp_[ind+1]-2
# 													map_[''.join(map(str,tmp))] += map_[''.join(map(str,tmp_))]

# 											for ind in range(6):
# 												flag = True
# 												for j in range(ind,ind+5):
# 													if tmp[j] < 1:
# 														flag = False
# 														break
# 												if flag == True:
# 													tmp_ = [x for x in lst]
# 													for j in range(ind,ind+5):
# 														tmp_[j] = tmp_[j] - 1
# 													map_[''.join(map(str,tmp))] += map_[''.join(map(str,tmp_))]			
# print(map_[''.join(map(str,tmp))])
													
