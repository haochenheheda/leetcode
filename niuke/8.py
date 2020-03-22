n = 21
w = 1165911996
v = [842104736,130059605,359419358,682646280,378385685,622124412,740110626,814007758,557557315,40153082,542984016,274340808,991565332,765434204,225621097,350652062,714078666,381520025,613885618,64141537,783016950]

v.sort()
num = 1
tmp_w_list = [0]
for i in range(n):
	one_stage_list = []
	tmp_w_list1 = [x for x in tmp_w_list]
	for tmp_w in tmp_w_list:
		if v[i] + tmp_w <= w:
			num += 1
			one_stage_list.append(v[i] + tmp_w)
		else:
			tmp_w_list1.remove(tmp_w)
	tmp_w_list = tmp_w_list1 + one_stage_list

print(num)

# def count(v,w):
# 	if sum(v) **2 < w:
# 		return 2 ** len(v)
# 	if len(v) == 0:
# 		return 1
# 	if v[0] > w:
# 		return count(v[1:],w)
# 	else:
# 		return count(v[1:],w - v[0]) + count(v[1:],w)

# print(count(v,w))

