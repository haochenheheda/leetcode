// prob9.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
class Solution {
public:
	bool isPalindrome(int x) {
		if (x >= 0 && x < 10) return true;
		if (x < 0 || x % 10 == 0) return false;
		int tmp = 0;
		for (; tmp * 10 <= x / 10; tmp = tmp * 10 + x % 10, x = x / 10);
		return (x == tmp || x / 10 == tmp);
	}
};
int main()
{
	Solution s;
	int x = 1001;
    std::cout << s.isPalindrome(x); 
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
