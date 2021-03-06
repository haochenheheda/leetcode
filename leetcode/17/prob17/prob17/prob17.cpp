// prob17.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	vector<string> letterCombinations(string digits) {
	map<string, string> MAP;
	MAP["2"] = "abc", MAP["3"] = "def", MAP["4"] = "ghi", MAP["5"] = "jkl"; 
	MAP["6"] = "mno",MAP["7"] = "pqrs", MAP["8"] = "tuv", MAP["9"] = "wxyz";
	vector<string> re;
	int ind = 0;
	string tmp = "";
	dfs(MAP, re, digits, ind, tmp);
	return re;
	}
private:

	void dfs(map<string,string> &MAP, vector<string> &re,string &digits,int ind,string tmp) {
		if (ind == digits.size()) {
			if (tmp != "") re.push_back(tmp);
			return;
		}
		for (char s : MAP[digits.substr(ind, 1)]) {
			dfs(MAP, re, digits, ind + 1, tmp + s);
		}
	
	}
};
int main()
{
	Solution s;
	string digits = "23";
	vector<string> re = s.letterCombinations(digits);
	for (int i = 0; i < re.size(); i++) printf("%s ",re[i]);
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
