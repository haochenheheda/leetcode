// prob14.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0) return "";
		int l = 0;
		int r = strs.size() - 1;
		return dc(strs, l, r);
	}
private:
	string dc(vector<string>& strs, int l, int r) {
		if (l == r) return strs[l];
		int mid = (l + r) / 2;
		string s1 = dc(strs, l, mid);
		string s2 = dc(strs, mid+1, r);
		int ind = 0;
		while (ind < s1.size() && ind < s2.size()) {
			if (s1[ind] != s2[ind]) break;
			ind += 1;
		}
		return s1.substr(0, ind);
	}
};
int main()
{
	Solution s;
	vector<string> x = { "flower","flow","flight" };
    std::cout << s.longestCommonPrefix(x); 
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
