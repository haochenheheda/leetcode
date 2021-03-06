// prob29.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	int divide(int dividend, int divisor) {
		if (dividend == 0) return 0;
		if (divisor == 1) return dividend;
		if (divisor == -1) {
			if (dividend > INT_MIN) return -dividend;// 只要不是最小的那个整数，都是直接返回相反数就好啦
			return INT_MAX;// 是最小的那个，那就返回最大的整数啦
		}
		long a = dividend;
		long b = divisor;
		int sign = 1;
		if ((a > 0 && b < 0) || (a < 0 && b>0)) {
			sign = -1;
		}
		a = a > 0 ? a : -a;
		b = b > 0 ? b : -b;
		long res = div(a, b);
		if (sign > 0)return res > INT_MAX ? INT_MAX : res;
		return -res;
	}
	int div(long a, long b) {  // 似乎精髓和难点就在于下面这几句
		if (a < b) return 0;
		long count = 1;
		long tb = b; // 在后面的代码中不更新b
		while ((tb + tb) <= a) {
			count = count + count; // 最小解翻倍
			tb = tb + tb; // 当前测试的值也翻倍
		}
		return count + div(a - tb, b);
	}
};

int main()
{
    Solution s;
	s.divide(100000, 1);
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
