// prob22.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	vector<string> generateParenthesis(int n) {
		dfs(n, 0, "");
		return re;
	}
private:
	vector<string> re;
	void dfs(int n, int stack, string tmp) {
		if (n == 0) {
			while (stack > 0) {
				tmp += ')';
				stack -= 1;
			}
			re.push_back(tmp);
		}
		else {
			dfs(n - 1, stack + 1, tmp + '(');
			if (stack > 0) {
				stack--;
				dfs(n, stack, tmp + ')');
			}
		}

	}
};
int main()
{
	Solution s;
    s.generateParenthesis(3); 
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
