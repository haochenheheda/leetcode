// prob15.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) {
		sort(nums.begin(),nums.end());
		vector<vector<int>> re;
		for (int i = 0; i < nums.size(); i++) {
			if (i > 0 && nums[i] == nums[i - 1]) continue;
			int l = i + 1;
			int r = nums.size() - 1;
			while (l < r) {
				if (nums[i] + nums[l] + nums[r] == 0) {
					re.push_back({ nums[i],nums[l],nums[r] });
					l += 1;
					r -= 1;
					while (l < nums.size() && nums[l] == nums[l - 1]) l += 1;
					while (r > 0 && nums[r] == nums[r + 1]) r -= 1;
				}
				else if (nums[i] + nums[l] + nums[r] > 0) {
					r -= 1;
				}
				else {
					l += 1;
				}
			}
		}
		return re;
	}
};
int main()
{
	Solution s;
	vector<int> nums = { -1, 0, 1, 2, -1, -4 };
	s.threeSum(nums);
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
