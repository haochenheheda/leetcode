// prob28.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	int strStr(string haystack, string needle) {
		if (needle == "") return 0;
		if (haystack.size() < needle.size()) return -1;
		for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
			bool flag = true;
			for (int j = 0; j < needle.size(); j++) {
				if (haystack[j + i] != needle[j]) { flag = false; break; }
			}
			if (flag) return i;

		}
		return -1;
	}
};
int main()
{
	Solution s;
	string h = "abb";
	string n = "abaaa";
	int x = s.strStr(h,n); 
	printf("%d", x);
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
