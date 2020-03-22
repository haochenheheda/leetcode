import bisect
m = int(raw_input().strip())
out = []
for _ in range(m):
    bisect.insort(out,int(raw_input().strip()[-6:]))
for i in out:
    print(i)