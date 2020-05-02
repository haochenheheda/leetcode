class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag = True
        for i in range(9):
        	row_tmp = [False] * 10
        	col_tmp = [False] * 10
        	for j in range(9):
        		if board[i][j] != '.':
        			if row_tmp[int(board[i][j])] == False:
        				row_tmp[int(board[i][j])] = True
        			else:
        				flag = False
        				break
        		if board[j][i] != '.':
        			if col_tmp[int(board[j][i])] == False:
        				col_tmp[int(board[j][i])] = True
        			else:
        				flag = False
        				break        		
        	if flag == False:
        		break
        for m in range(3):
        	for n in range(3):
        		rect_tmp = [False] * 10
        		for i in range(3):
        			for j in range(3):
        				if board[3*m + i][3*n + j] != '.':
        					if rect_tmp[int(board[3*m + i][3*n + j])] == False:
        						rect_tmp[int(board[3*m + i][3*n + j])] = True
        					else:
        						flag = False
        						break

        return flag

if __name__ == '__main__':
	s = Solution()
	board = [
			["8","3",".",".","7",".",".",".","."],
			["6",".",".","1","9","5",".",".","."],
			[".","9","8",".",".",".",".","6","."],
			["8",".",".",".","6",".",".",".","3"],
			["4",".",".","8",".","3",".",".","1"],
			["7",".",".",".","2",".",".",".","6"],
			[".","6",".",".",".",".","2","8","."],
			[".",".",".","4","1","9",".",".","5"],
			[".",".",".",".","8",".",".","7","9"]
]
	print(s.isValidSudoku(board))