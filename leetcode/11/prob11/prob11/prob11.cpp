// prob11.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
#define max(a,b) ((a>b)?a:b)
#define min(a,b) ((a<b)?a:b)
using namespace std;
class Solution {
public:
	int maxArea(vector<int>& height) {
		return shuangzhizhen(height);
	}
private:
	int baoli(vector<int>& height) {
		int max_ = 0;
		for (int i = 0; i < height.size()-1; i++) {
			for (int j = i + 1; j < height.size(); j++) {
				max_ = max(max_, (j - i) * min(height[i],height[j]));
			}
		}
		return max_;
	}
	int shuangzhizhen(vector<int>& height){
		int ind1 = 0;
		int ind2 = height.size()-1;
		int max_ = (ind2 - ind1) * min(height[ind1], height[ind2]);
		while (ind1 < ind2) {
			if (height[ind1] < height[ind2]) {
				ind1 += 1;
			}
			else {
				ind2 -= 1;
			}
			max_ = max(max_, (ind2 - ind1) * min(height[ind1], height[ind2]));
			
		}
		return max_;
	}
};
int main()
{
	Solution s;
	vector<int> lst = { 1,8,6,2,5,4,8,3,7 };
	printf("%d", s.maxArea(lst));

	//for (int i = 0; i < 9; i++) printf("%d ", lst[i]);
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
