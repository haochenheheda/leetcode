n = 3
m = 9
c = [1,1,2,2,2,3,1,2,3]
score = [0] * n
for i in c:
	score[i-1] += 1
print(min(score))