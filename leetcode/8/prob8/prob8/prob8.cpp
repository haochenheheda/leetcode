// prob8.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	int myAtoi(string str) {
		const char *p = str.c_str();
		for (; p != nullptr && *p == ' '; p++);
		if (p == nullptr || (*p != '+' && *p != '-' && (*p < '0' || *p > '9'))) return 0;
		int re = 0;
		int flag = 1;
		if (*p == '+') p++;
		else if (*p == '-') { flag = -1; p++;}
		while (p != nullptr) {
			if (*p >= '0' && *p <= '9') {
				if (flag == 1 && (INT_MAX - (*p - '0')) / 10 < re) return INT_MAX;
				if (flag ==-1 && (INT_MAX - (*p - '0')) / 10 < re) return INT_MIN;
				re = re * 10 + (*p - '0');
				p++;
			}
			else break;
		}
		return flag * re;
	}
};

int main()
{
    Solution s;
	string x = "+-3";
	printf("%d",s.myAtoi(x));
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
