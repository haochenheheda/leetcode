import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n,m,k = map(int,lines[0].strip().split())
map_ = {}
for line in lines[1:1+k]:
	x_,y_,c = map(int,line.strip().split())
	map_[m*x_+y_] = c
t = int(lines[1+k].strip())
x = range(n)
y = range(m)
for line in lines[k+2:]:
	q,x_,y_ = map(int,line.strip().split())
	if q == 2:
		if map_.has_key(m*x[x_]+y[y_]):
			print(map_[m*x[x_]+y[y_]])
		else:
			print(-1)
		#print(map_.setdefault(m*x[x_]+y[y_],-1))
	elif q == 1:
		y[x_],y[y_] = y[y_],y[x_]
	elif q == 0:
		x[x_],x[y_] = x[y_],x[x_]
