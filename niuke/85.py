import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
ab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
map_ = {str(i+1):j for i,j in enumerate(ab)}
def decode(lst,map_,re):
	if len(lst) == 0:
		re_list.append(re)
	elif len(lst) == 1:
		re_list.append(re + map_[lst[-1]])
	else:
		if int(lst[:2]) <= 26 and int(lst[:2]) >= 10:
			decode(lst[2:],map_,re + map_[lst[:2]])
		if int(lst[0]) > 0:
			decode(lst[1:],map_,re + map_[lst[0]])


for line in lines:
	lst = line.strip()
	re_list = []
	re = ''
	decode(lst,map_,re)
	re_list.sort()
	out = ''
	for re in re_list:
		out += (re + ' ')
	print(out[:-1])



