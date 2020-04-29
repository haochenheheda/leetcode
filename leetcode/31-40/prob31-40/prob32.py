# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         num = 0
#         max_num_l = 0
#         max_stack = []
#         stack = 0
#         ind_list = []
#         for i,s_ in enumerate(s):
#         	if s_ == '(':
#         		stack += 1
#         	else:
#         		if stack > 0:
#         			stack -= 1
#         			num += 1
#         			if num > max_num_l:
#         				ind_list = [i]
#         				max_num_l = num
#         				max_stack = [stack]
#         			elif num == max_num_l:
#         				ind_list.append(i)
#         				max_stack.append(stack)

#         		else:
#         			print(i)
#         			if num > max_num_l:
#         				ind_list = [i-1]
#         				max_stack = [stack]
#         				max_num_l = num
#         			elif num == max_num_l:
#         				ind_list.append(i-1)
#         				max_stack.append(stack)
#         			num = 0
#         			stack = 0
#         print(max_num_l,max_stack,ind_list,ind_list[0]-max_num_l*2-max_stack[0])
#         print(s[ind_list[0]-max_num_l*2-max_stack[0]+1:ind_list[0]+1-36])
#         max_num_r_f = 0 
#         for ind,last_stack in zip(ind_list,max_stack):
# 	        stack = 0
# 	        max_num_r = 0
# 	        num = 0
#         	for j in range(ind,ind - 2*max_num_l - last_stack,-1):
#         		print(stack,num,s[j])
#         		if s[j] == ')':
#         			stack += 1
#         		else:
#         			if stack > 0:
#         				stack -= 1
#         				num += 1
#         				max_num_r = max(max_num_r,num)
#         			else:
#         				max_num_r = max(max_num_r,num)
#         				num = 0
#         				stack = 0
#         	max_num_r_f = max(max_num_r_f,max_num_r)
    
#         return max_num_r_f*2
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(1,len(s)):
            if s[i] == '(':
                continue
            else:
                if s[i-1] == '(':
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i-2] + 2
                else:
                    if i-1-dp[i-1]>= 0 and s[i-1-dp[i-1]] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]
        return max(dp)
if __name__ == '__main__':
	s = Solution()
	lst = "(()())"
	print(s.longestValidParentheses(lst))