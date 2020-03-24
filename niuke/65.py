m,k = map(int,raw_input().strip().split())
lst = list(map(int,raw_input().strip().split()))
out = []
r = m%k
d = m/k
if r != 0:
	out += lst[-r:]
for i in range(d,0,-1):
	out += lst[(i-1) * k: i * k]
re = ''
for i in out:
	re += (str(i) + ' ')
print(re.strip())
