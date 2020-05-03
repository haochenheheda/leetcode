class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        left_pos = []
        stack = []
        for i in range(9):
        	for j in range(9):
        		if board[i][j] == '.':
        			left_pos.append([i,j])
        ind = 0
        start = 1
        while len(stack) < len(left_pos):
        	y,x = left_pos[ind]
    		for i in range(start,11):
        		if self.isvalid(x,y,str(i),board):
        			board[y][x] = str(i)
        			break
        	if board[y][x] == '10':
        		board[y][x] = '.'
        		ind -= 1
        		start = stack.pop(-1) + 1

        	else:
        		stack.append(int(board[y][x]))
        		ind += 1
        		start = 1
        	#print(stack)

        				


    def isvalid(self,x,y,num,board):
    	for i in range(9):
    		if board[y][i] == num:
    			return False
    		if board[i][x] == num:
    			return False
    	for i in range(3):
    		for j in range(3):
    			if board[y/3*3+i][x/3*3+j] == num:
    				return False
    	return True

if __name__ == '__main__':
	s = Solution()
	board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s.solveSudoku(board)
print(board)