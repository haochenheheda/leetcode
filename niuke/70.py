lst = list(map(int,raw_input().strip().split()))
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
map_ = {k:v for k,v in zip(letter,lst)}
s = raw_input().strip()

row_count = 0
col_count = 0
for s_ in s:
	col_count += map_[s_]
	if col_count > 100:
		col_count = map_[s_]
		row_count += 1
print(str(row_count+1) + ' ' + str(col_count))
