n = int(raw_input().strip())
j = 1
for i in range(1,n+1):
	j *= i
	while j % 10 == 0:
		j /= 10
	j = j%100

print(j%10)