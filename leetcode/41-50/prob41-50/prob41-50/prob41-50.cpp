// prob41-50.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
/*          prob 41           */
class Solution41 {
public:
	int firstMissingPositive(vector<int>& nums) {
		int n = nums.size();
		if (n == 0) return 1; 
		for (int i = 0; i < n; i++) {
			while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
				swap(nums[nums[i] - 1], nums[i]);
			}
		}
		int re = 0;
		for (; re < n; re++) {
			if (nums[re] != re + 1) return re + 1;
		}
		return re + 1;
	}
};

/*           prob 42             */
class Solution42 {
public:
	int trap(vector<int>& height) {
		if (height.size() == 0) return 0;
		int max_ = 0;
		int ind = 0;
		int sum_ = 0;
		for (int i = 0; i < height.size(); i++) max_ = max(max_, height[i]);
		int tmp_max = 0;
		for (; ind < height.size(); ind++) {
			if (height[ind] > tmp_max) tmp_max = height[ind];
			sum_ += tmp_max;
			sum_ -= height[ind];
			if (tmp_max == max_) break;
		}
		tmp_max = 0;
		for (int i = height.size() - 1; i > ind; i--) {
			if (height[i] > tmp_max) tmp_max = height[i];
			sum_ += tmp_max;
			sum_ -= height[i];
		}
		return sum_;
	}
};

/*           prob 43             */
class Solution {
public:
	string multiply(string num1, string num2) {
		int l1 = num1.size(), l2 = num2.size();
		vector<int> re(l1+l2,0);
		int n1 = 0, n2 = 0;
		for (int i = l1 - 1; i >= 0; i--) {
			for (int j = l2 - 1; j >= 0; j--) {
				n1 = num1[i] - '0';
				n2 = num2[j] - '0';
				int tmp = n1 * n2 + re[i + j + 1];
				re[i + j + 1] = tmp % 10;
				re[i + j] += tmp / 10;
			}
		}
		int i = 0;
		for (; i < l1 + l2 && re[i] == 0; i++);
		string x = "";
		for (; i < l1 + l2; i++) x.push_back(re[i] + '0');
		if (x == "") return "0";
		return x;
	}
};

int main()
{
	Solution s;
    std::cout << s.multiply("2","3"); 
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
