// solu12.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
	string intToRoman(int num) {
		vector<int> value = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
		vector<string> symbol = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
		string s = "";
		while (num) {
			int i = 0;
			for (;i < 13;i ++){
				if (value[i] <= num) break;
			}
			s += symbol[i];
			num -= value[i];

		}
		return s;

	}
};
int main()
{
	Solution s;
	int num = 1994;
    std::cout << s.intToRoman(num); 
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
