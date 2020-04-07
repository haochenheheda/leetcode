#pragma once
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
	string convert(string s, int numRows) {
		if (numRows == 1) return s;
		vector<string> s_lst(numRows);
		for (int i = 0; i < s.length(); i++) {
			int r = i % (2 * numRows - 2);
			if (r < numRows) {
				s_lst[r] += s[i];
			}
			else {
				s_lst[2 * numRows - r - 2] += s[i];
			}
		}
		string re = "";
		for (string s_ : s_lst) {
			re += s_;
		}
		return re;
	}
};