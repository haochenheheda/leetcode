// prob10.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
	bool isMatch(string s, string p) {
		int pl = p.size();
		int sl = s.size();
		int **dp = new int*[pl + 1];
		for (int i = 0; i < pl + 1; i++) {
			dp[i] = new int[sl + 1];
			for (int j=0; j < sl + 1; j++) dp[i][j] = 0;
		}
		int tmp = 0;
		dp[pl][sl] = 1;
		for (int i = pl - 1; i >= 0; i--) {
			if (p[i] == '*') {
				tmp = 1;
				for (int j = sl; j >= 0; j--) {
					dp[i][j] = dp[i + 1][j];
				}
			}
			else {
				if (tmp) {
					for (int j = sl; j >= 0; j--) {
						if (dp[i + 1][j]) {
							dp[i][j] = 1;
							for (int j_ = j-1; j_ >= 0; j_--) {
								if (p[i] == s[j_] ||p[i] == '.') dp[i][j_] = 1;
								else break;
							}
						}
					}


				}	
				else {
					for (int j = sl - 1; j >= 0; j--) {
						if (dp[i+1][j+1] &&( s[j] == p[i] || p[i] == '.')) {
							dp[i][j] = 1;
						}
					}
				}
				tmp = 0;
			}
		}
		/*for (int i = 0; i < pl + 1; i++) {
			for (int j = 0; j < sl + 1; j++) {
				printf("%d", dp[i][j]);
				printf(" ");
			}
			printf("\n");
		}*/
		return dp[0][0];
	}
};
int main()
{	
	string s = "mississippi";
	string p = "mis*is*ip*.";
	Solution so;
    printf("%d",so.isMatch(s,p)); 
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
