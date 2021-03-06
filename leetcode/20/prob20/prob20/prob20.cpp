// prob20.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	bool isValid(string s) {
		vector<char> stack = {};
		bool flag = true;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '(' || s[i] == '[' || s[i] == '{') stack.push_back(s[i]);
			else if (stack.size() > 0 && ((s[i] == ')' && stack[stack.size()-1] == '(')|| (s[i] == ']' && stack[stack.size()-1] == '[')|| (s[i] == '}' && stack[stack.size()-1] == '{'))) stack.pop_back();
			else {
				flag = false; break;
			}

		}
		return flag && stack.size()==0;
	}
};
int main()
{
	Solution s;
	string s_ = "()[]{}";
    std::cout << s.isValid(s_); 
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
