str_ = raw_input().strip()
lst = [0] * 26
ref = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for s in str_:
	lst[ref.index(s)] += 1

out = ''
for i,n in enumerate(lst):
	if n > 0:
		out += (ref[i] + str(n))
print(out)