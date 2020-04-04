#pragma once
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int size = s.size();
		int l = 0;
		int max = 0;
		for (int r = 0; r < size; r++) {
			int l_ = l;
			for (int l_ = l; l_ < r; l_++) {
				if (s[l_] == s[r]) {
					l = l_ + 1;
					break;
				}
					
			}
			if (max < r - l + 1) max = r - l + 1;

		}
		return max;
	}
};