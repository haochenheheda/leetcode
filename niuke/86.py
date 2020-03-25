import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()
map_ = set()
for line in lines[:-1]:
	type_,ip = line.strip().split(':')
	if type_ == 'i':
		print('ok')
		map_.add(ip)
	if type_ == 'd':
		print('ok')
		map_.remove(ip)
	if type_ == 's':
		if ip in map_:
			print('true')
		else:
			print('false')

