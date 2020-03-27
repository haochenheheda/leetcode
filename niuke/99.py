import sys
# lines = sys.stdin.readlines()
tree = {}
num = {}
lines = open('input.txt','r').readlines()
for line in lines[1:]:
	set_ = list(map(int,line.strip().split()))
	p = set_[0]
	if not num.has_key(p):
		num[p] = 0
	for i in set_:
		if not tree.has_key(i):
			tree[i] = p
			num[p] += 1
		else:
			while tree[i] != p:
				next_ = tree[i]
				tree[i] = p
				i = next_
			if i != p and num.has_key(i):
				num[p] += num[i]
				num.pop(i)

print(len(num.keys()))
print(max(num.values()))
