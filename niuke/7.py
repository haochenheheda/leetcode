import sys
lines = ['3\n', '5 0\n', '6 0\n', '7 0\n', '59\n', '6 59\n']
n = int(lines[0].strip())
alert = []
for line in lines[1:-2]:
	h,m = line.strip().split()
	time = 60 * int(h) + int(m)
	alert.append(time)
alert.sort()
cost = int(lines[-2].strip())
start_h,start_w = lines[-1].strip().split()
start_time = 60 * int(start_h) + int(start_w)
gt_time = start_time - cost

for i in range(len(alert)-1,-1,-1):
	if alert[i]<=gt_time:
		print(str(alert[i]/60) + ' ' + str(alert[i]%60))
		break
