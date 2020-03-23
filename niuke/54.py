# s.startswith
# eval
# yong di gui shi xian dfs
#append,sort fan hui zhi shi None!!
# list cao zuo: lst.append([a]) bu chong xin fen pei nei cun lst += [a] ye bu chong xin fen pei
# dan shi lst + [a] hui chong xin fen pei, lst + [a] fan hui yi ge xin di zhi,bu gai bian yuan lai de lst
s=raw_input().split('"')[-2]
ss=raw_input().split('"')
words=[]
i=1
while i<len(ss)-1:
    words.append([len(ss[i]),ss[i]])
    i+=1
words.sort()
word_list=[x[1] for x in words[::-1]]

res_all = []

def dfs(s,word_list,res_list):
	if not len(s):
		res_all.append(res_list)
	else:
		for w in word_list:
			if s.startswith(w):
				dfs(s[len(w):],word_list,res_list + [w])

dfs(s,word_list,[])
print(res_all)




# stack = [0]
# ind = 0
# res = []
# while len(stack) > 0:
# 	# print(stack)
# 	status = stack[-1]
# 	if word_list[status] == s[ind:ind+len(word_list[status])]:
# 		ind += len(word_list[status])
# 		if ind == len(s):
# 			str_ = ''
# 			for s_ in stack:
# 				str_ += (word_list[s_] + ' ')
# 			res.append(str_.strip())
# 			# print(res)
# 			ind -= len(word_list[stack[-1]])
# 			stack[-1] += 1
# 		else:
# 			stack += [0]
# 	else:
# 		stack[-1] += 1
# 	while len(stack) > 0 and stack[-1] >= len(word_list):
# 		stack.pop(-1)
# 		if len(stack) == 0:
# 			break
# 		ind -= len(word_list[stack[-1]])
# 		stack[-1] += 1
# if not res:
#     print '[]'
# else:
#     s='['
#     for x in res:
#         s+=x+', '
#     s=s[:-2]+']'
#     print s