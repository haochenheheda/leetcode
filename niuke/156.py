n = int(raw_input().strip())
lst = map(int,raw_input().strip().split())
m = 0
for l in lst:
    m += (l-1)
print(m)