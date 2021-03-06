// prob16.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		sort(nums.begin(), nums.end());
		int min = INT_MAX;
		int re;
		for (int i = 0; i < nums.size() - 2; i++)
		{
			int l = i + 1;
			int r = nums.size() - 1;
			while (l < r) {
				int d = nums[i] + nums[l] + nums[r] - target;
				if (abs(d) < min) {
					min = abs(d);
					re = d + target;
				}
				if (d > 0) {
					r--;
					while (r > i && nums[r + 1] == nums[r]) r--;
				}
				else if (d < 0) {
					l++;
					while (l < nums.size() - 1 && nums[l - 1] == nums[l]) l++;
				}
				else break;
			}
			if (min == 0) break;
		}
		return re;
	}
};
int main()
{
	Solution s;
	vector<int> nums = { -1,2,1,-4 };
	int target = 2;
	printf("%d", s.threeSumClosest(nums, target));
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
