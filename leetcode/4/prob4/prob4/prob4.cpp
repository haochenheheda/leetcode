// prob4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include "solu1.h"
#include "solu2.h"
int main()
{	

	vector<int> nums1;
	vector<int> nums2;
	nums1.push_back(1);
	nums1.push_back(3);
	nums2.push_back(2);
	nums2.push_back(4);
	nums2.push_back(5);
	Solution1 s;
    std::cout << s.findMedianSortedArrays(nums1,nums2); 
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
