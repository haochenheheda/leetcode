x = raw_input().strip()
c_num = 0
weishu = len(x)
sum_ = 0
# for i in range(1,weishu):
# 	sum_ += 6 * 7 ** (i-1) - 2 * 3 ** (i-1)

flag = 0
big = {'0':1,'1':2,'2':3,'3':3,'4':3,'5':4,'6':5,'7':5,'8':6,'9':7}
small = {'0':1,'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':3,'9':3}

for i,x_ in enumerate(x):
	if i > 0 and i < weishu-1:
		if int(x_) > 0:
			if flag == 1:
				sum_ += big[str(int(x[i])-1)] * (7 ** (weishu-1 - i))
			else:
				big_ = (big[str(int(x[i])-1)]) * (7 ** (weishu-1 - i))
				small_ = (small[str(int(x[i])-1)]) * (3 ** (weishu-1 - i))
				sum_ += (big_ - small_)
		


		if x_ in ['3','4','7']:
			break
		if x_ in ['2','5','6','9']:
			flag = 1		
	elif i == weishu-1:
		if flag == 1:
			sum_ += big[x_]
		else:
			sum_ += big[x_] - small[x_]
	else:
		big_ = (big[str(int(x[i])-1)]) * (7 ** (weishu-1 - i))
		small_ = (small[str(int(x[i])-1)]) * (3 ** (weishu-1 - i))
		sum_ += (big_ - small_)
		if x_ in ['3','4','7']:
			break
		if x_ in ['2','5','6','9']:
			flag = 1

print(sum_)