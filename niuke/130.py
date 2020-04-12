import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
n,m = map(int,lines[0].strip().split())
x,y = map(int,lines[1].strip().split())
map_ = [i.strip() for i in lines[2:]]
searched_map = [[False] * m for _ in range(n)]
def count_one(x,y):
	try:
		num = 0
		for x_ in range(x-1,x+2):
			for y_ in range(y-1,y+2):
				if x_ > 0 and x_ <= n and y_ > 0 and y_ <= m:
					if map_[x_-1][y_-1] == '*':
						num += 1
		map_[x-1] = map_[x-1][:y-1] + str(num) + map_[x-1][y:]
		searched_map[x-1][y-1] = True
		if num != 0:
			return 
		else:
			for x_ in range(x-1,x+2):
				for y_ in range(y-1,y+2):
					if x_ > 0 and x_ <= n and y_ > 0 and y_ <= m and searched_map[x_-1][y_-1] == False:
						count_one(x_,y_)
	except:
		pass
if map_[x-1][y-1] == '*':
	print('GG')
else:
	count_one(x,y)
	for i in map_:
		print(i)

