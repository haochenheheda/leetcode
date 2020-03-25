import sys
# lines = sys.stdin.readlines()
lines = open('input.txt','r').readlines()



# for line in lines:
# 	text,pattern = line.strip().split()
# 	s = -1
# 	e = -1
# 	flag = False
# 	dp = [[0] * len(text) for _ in range(len(text))]
# 	for i in range(len(text)):
# 		if text[i] == pattern[0]:
# 			dp[0][i] = 1
# 	for k in range(1,len(text)):
# 		for i in range(len(text)-k):
# 			if i+k >= len(text):
# 				break
# 			if text[i+k] == pattern[dp[k-1][i]]:
# 				dp[k][i] = dp[k-1][i] + 1
# 			else:
# 				dp[k][i] = dp[k-1][i]
# 			if dp[k][i] == len(pattern):
# 				s = i
# 				e = i+k
# 				flag = True
# 				break
# 		if flag == True:
# 			break
# 	print(str(s) + ' ' + str(e))


for line in lines:
	text,pattern = line.strip().split()
	min_len = len(text)
	re_start = -1
	re_end = -1
	start_lst = []
	for i in range(len(text) - len(pattern) + 1):
		if text[i] == pattern[0]:
			start_lst.append(i)

	for i in start_lst:
		j = 0
		while True:
			if i > len(text)-1:
				break
			if text[i] == pattern[j]:
				if j == 0:
					start = i
				if j == len(pattern) - 1:
					end = i
					if min_len > end - start:
						min_len = end - start
						re_start = start
						re_end = end
					break
				i += 1
				j += 1
			elif text[i] != pattern[j]:
				i += 1
	print(str(re_start) + ' ' + str(re_end))

