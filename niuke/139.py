import collections
import sys
n,t = map(int,raw_input().strip().split())
lst = raw_input().strip()
dic = collections.OrderedDict()
for i in lst:
	dic[int(i)] = dic.setdefault(int(i),0) + 1

min_money = sys.maxint 
re = ''
for k,v in dic.items():
	left_num = t - v
	tmp_lst = lst + ''
	if left_num <= 0:
		min_money = 0
		re = tmp_lst
		break
	bias = 0
	add_num = 0
	money = 0
	# print('k,v',k,v)
	# print('left_num',left_num)
	while add_num < left_num:
		bias += 1
		add_num += dic.setdefault(k+bias,0) + dic.setdefault(k-bias,0)
		money += bias * (dic.setdefault(k+bias,0) + dic.setdefault(k-bias,0))
	money -= (add_num - left_num) * bias
	# print(money,min_money)
	if money < min_money:
		min_money = money
		for s in range(k-bias + 1,k+bias):
			tmp_lst = tmp_lst.replace(str(s),str(k))
		re_num = min(dic.setdefault(k+bias,0),left_num - (add_num - (dic.setdefault(k+bias,0) + dic.setdefault(k-bias,0))))
		re_num1 = left_num - (add_num - (dic.setdefault(k+bias,0) + dic.setdefault(k-bias,0))) - re_num
		tmp_lst = tmp_lst.replace(str(k+bias),str(k),re_num)
		tmp_lst = tmp_lst[::-1]
		tmp_lst = tmp_lst.replace(str(k-bias),str(k),re_num1)
		re = tmp_lst[::-1]

print(min_money)
print(re)
