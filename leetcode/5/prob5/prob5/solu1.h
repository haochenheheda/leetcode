#pragma once
#include <string>
#define min(a,b) ((a<b)?a:b)
using namespace std;
class Solution {
public:
	string longestPalindrome(string s) {
		string s_p = "^";
		for (int i = 0; i < s.size(); i++) {
			s_p = s_p + "#";
			s_p = s_p + s[i];
		}
		s_p += "#$";

		int c = 0;
		int r = 0;
		int max_start = 0;
		int max_l = 0;
		int *p = new int[s_p.size()];
		for (int i=1; i < s_p.size(); i++) {
			int mirror_i = 2 * c - i;
			if (i <= r) {
				p[i] = min(r - i, p[mirror_i]);
			}
			else {
				p[i] = 0;
			}
			while (i + p[i] + 1 < s_p.size() && s_p[i + p[i] + 1] == s_p[i - p[i] - 1]) {
				p[i] += 1;
			}
			if (max_l < p[i]) {
				max_l = p[i];
				max_start = (i - p[i]) / 2;
			}
			if (r < i + p[i]) {
				c = i;
				r = i + p[i];
			}
		}
		return s.substr(max_start, max_l);

	}
};