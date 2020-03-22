y,m,d = 1990,9,20
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
	days[1] = 29

sum_ = 0
for i in range(m-1):
	sum_ += days[i]
sum_ += d
print(sum_)