// prob18.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	vector<vector<int>> fourSum(vector<int>& nums, int target) {
		vector<vector<int>> re;
		sort(nums.begin(), nums.end());
		if (nums.size() < 4) return re;
		for (int i = 0; i < nums.size() - 3; i++) {
			if (i > 0 && nums[i] == nums[i - 1]) continue;
			for (int j = i + 1; j < nums.size() - 2; j++) {
				if (j > i + 1 && nums[j] == nums[j - 1]) continue;
				int l = j + 1;
				int r = nums.size() - 1;
				while (l < r) {
					if (nums[i] + nums[j] + nums[l] + nums[r] == target) {
						vector<int> tmp = { nums[i] , nums[j] , nums[l] , nums[r] };
						re.push_back(tmp);
						l += 1;
						r -= 1;
						while (l < r && nums[l] == nums[l - 1]) l++;
						while (l < r && nums[r] == nums[r + 1]) r--;
					}
					else if (nums[i] + nums[j] + nums[l] + nums[r] > target) {
						r--;
						while (l < r && nums[r] == nums[r + 1]) r--;
					}
					else {
						l++;
						while (l < r && nums[l] == nums[l - 1]) l++;
					}
				}
			}
		}
		return re;
	}
};
int main()
{
	Solution s;
	vector<int> nums = { 1, 0, -1, 0, -2, 2 };
	s.fourSum(nums, 0);
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
