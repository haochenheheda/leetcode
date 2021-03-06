// prob31-40.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*      prob 31       */
class Solution31 {
public:
	void nextPermutation(vector<int>& nums) {
		if (nums.size() == 1) return ;
		for (int i = nums.size() - 2; i >= 0; i--) {
			if (nums[i] < nums[i + 1]) {
				for (int j = i + 1; j < nums.size(); j++) {
					if (j == nums.size() - 1 || (nums[j] > nums[i] && nums[j + 1] <= nums[i])) {
						swap(nums[i], nums[j]);
						break;
					}
				}
				int l = i+1;
				int r = nums.size() - 1;
				while (l < r) {
					swap(nums[l++], nums[r--]);
				}
				return;
			}
		}
		int l = 0;
		int r = nums.size() - 1;
		while (l < r) {
			swap(nums[l++], nums[r--]);
		}
		return;

	}
};

/*       prob 32        */
class Solution32 {
public:
	int longestValidParentheses(string s) {
		if (s.size() == 0) return 0;
		int* dp = new int[s.size()] {0};
		int max_ = 0;
		for (int i = 1; i < s.size(); i++) {
			if (s[i] == '(');
			else {
				if (s[i - 1] == '(') { dp[i] = (i == 1) ? 2 : dp[i - 2] + 2; max_ = max(max_, dp[i]); }
				else {
					if (i - 1 - dp[i - 1]>=0&&s[i - 1 - dp[i - 1]] == '(') {
						
						dp[i] = (i - 2 - dp[i - 1]>=0)?dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]: dp[i - 1] + 2;
						max_ = max(max_, dp[i]);
					}
				}
			}
		}
		return max_;

	}
};

/*       prob 33          */
class Solution33 {
public:
	int search(vector<int>& nums, int target) {
		int l = 0;
		int r = nums.size() - 1;
		int m = 0;
		while (l <= r) {
			m = (l + r) / 2;
			if (nums[m] == target) return m;
			else if (nums[m] < target) {
				if (nums[l] < nums[m]) l = m + 1;
				else {
					if (nums[r] >= target) l = m + 1;
					else r = m - 1;
				}
			}
			else {
				if (nums[r] > nums[m]) r = m - 1;
				else {
					if (nums[l] <= target) r = m - 1;
					else l = m + 1;
				}
			
			}
		}
		return -1;
	}
};


/*            prob 34              */
class Solution34 {
public:
	vector<int> searchRange(vector<int>& nums, int target) {
		vector<int> result = {-1,-1};
		if (nums.size() == 0) return result;
		int l = 0;
		int r = nums.size() - 1;
		int m = 0;
		while (l < r) {
			m = (l + r) / 2;
			if (nums[m] >= target) r = m;
			else l = m + 1;
		}
		if (nums[l] != target) return result;
		else result[0] = l;

		r = nums.size() - 1;
		while (l < r) {
			m = (l + r) / 2 + (l + r) % 2;
			if (nums[m] <= target) l = m;
			else r = m - 1;
		}
		result[1] = l;
		return result;
	}
};


/*            prob 35            */
class Solution35 {
public:
	int countAndSay(vector<int>& nums, int target) {
		if (target < nums[0]) return 0;
		if (target > nums[nums.size()-1]) return nums.size();
		int l = 0, r = nums.size() - 1,m = 0;
		while (l < r) {
			m = (l + r) / 2;
			if (nums[m] == target) return m;
			else if (nums[m] > target) r = m;
			else l = m + 1;
		}
		return l;
	}
};

/*            prob 36            */

class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		vector<vector<int>> row(10,vector<int>(10,0));
		vector<vector<int>> col(10, vector<int>(10, 0));
		vector<vector<int>> sub(10, vector<int>(10, 0));
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] != '.') {
					int tmp = board[i][j] - '0';
					if (row[i][tmp] == 0 && col[j][tmp] == 0 && sub[i / 3 * 3 + j / 3][tmp] == 0) {
						row[i][tmp] ++; col[j][tmp] ++; sub[i / 3 * 3 + j / 3][tmp]++;
					}
					else return false;
				}
			}
		}
		return true;
	}
};


/*             prob 37              */
class Solution37 {
public:
	void solveSudoku(vector<vector<char>>& board) {
		vector<int> stack = {};
		vector<vector<int>> pos = {};
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] == '.') pos.push_back({ i,j });
			}
		}
		int start = 1;
		int ind = 0;
		while (stack.size() < pos.size()) {
			int y = pos[ind][0];
			int x = pos[ind][1];
			for (int i = start; i < 11; i++) {
				if (isvalid(x, y, i + '0', board)) {
					board[y][x] = i + '0';
					break;
				}
			}
			if (board[y][x] == '0' + 10) {
				board[y][x] = '.';
				ind -= 1;
				start = stack[stack.size() - 1] + 1;
				stack.pop_back();
			}
			else {
				stack.push_back(board[y][x] - '0');
				ind += 1;
				start = 1;
			}

		}

	}
private:
	bool isvalid(int x, int y, char num, vector<vector<char>>& board) {
		for (int i = 0; i < 9l; i++) {
			if (board[y][i] == num) return false;
			if (board[i][x] == num) return false;
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (board[y / 3 * 3 + i][x / 3 * 3 + j] == num) return false;
			}
		}
		return true;
	}
};


/*            prob 38            */
class Solution38 {
public:
	string countAndSay(int n) {
		string num = "1";
		if (n == 1) return num;
		else {
			for (int i = 1; i < n; i++) {
				string tmp = "";
				int times = 1;
				num += 'x';
				for (int j = 1; j < num.size(); j++) {
					if (num[j] != num[j - 1]) {
						tmp += (times + '0');
						tmp += num[j - 1];
						times = 1;
					}
					else {
						times++;
					}
				}
				num = tmp;
			}
			return num;	
		}
	}
};


/*            prob 39              */
class Solution39 {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		sort(candidates.begin(),candidates.end());
		vector<vector<int>> res = {};
		dfs(candidates, 0, 0, {}, target, res);
		return res;
	}
private:
	void dfs(vector<int>& candidates,int tmp_sum,int i,vector<int> re,int target, vector<vector<int>> & res) {
		if (tmp_sum == target) { res.push_back(re); return; }
		if (i == candidates.size()) return;
		for (int j = i; j < candidates.size(); j++) {
			if (tmp_sum + candidates[j] > target) return;
			else {
				re.push_back(candidates[j]);
				dfs(candidates, tmp_sum + candidates[j], j, re, target, res);
				re.pop_back();
			}
		}
	}
};

/*            prob 39              */
class Solution {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		sort(candidates.begin(), candidates.end());
		vector<vector<int>> res = {};
		dfs(candidates, 0, -1, {}, target, res);
		return res;
	}
private:
	void dfs(vector<int>& candidates, int tmp_sum, int i, vector<int> re, int target, vector<vector<int>> & res) {
		if (tmp_sum == target) { res.push_back(re); return; }
		if (i == candidates.size()) return;
		for (int j = i+1; j < candidates.size(); j++) {
			if (j > i + 1 && candidates[j] == candidates[j - 1]) continue;
			if (tmp_sum + candidates[j] > target) return;
			else {
				re.push_back(candidates[j]);
				dfs(candidates, tmp_sum + candidates[j], j, re, target, res);
				re.pop_back();
			}
		}
	}
};

int main()
{
	Solution38 s;
	int nums = 5;
	s.countAndSay(nums);
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
