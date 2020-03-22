n = 6
k = 3
a = [1,3,5,2,5,4]
t = [1,1,0,1,0,0]


e = []
s = 0
for i in range(n):
	e.append(a[i] * (1 - t[i]))
	s += t[i] * a[i]
plus = 0
max_plus = 0
start_ind = t.index(0)
end_ind = n - k + 1
for i in range(end_ind,0,-1):
	if t[i - 2 + k] == 0:
		end_ind = i
		break
for i in range(start_ind,end_ind):
	if i == start_ind:
		plus = sum(e[start_ind:start_ind + k])
	else:
		plus = plus - e[i-1] + e[i+k-1]
	if plus > max_plus:
		max_plus = plus
print(max_plus + s)