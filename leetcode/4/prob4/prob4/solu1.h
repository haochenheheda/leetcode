#pragma once
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		double tmp = 0;
		double tmp1 = 0;
		int len1 = nums1.size();
		int len2 = nums2.size();
		int ind1 = 0;
		int ind2 = 0;
		if ((len1 + len2) % 2 == 1) {
			while ((ind1 + ind2) <= (len1 + len2) / 2) {
				if (ind1 == len1) {
					tmp = nums2[ind2];
					ind2 ++;
				}
				else if (ind2 == len2) {
					tmp = nums1[ind1];
					ind1++;
				}
				else {
					if (nums1[ind1] <= nums2[ind2]) {
						tmp = nums1[ind1];
						ind1++;
					}
					else {
						tmp = nums2[ind2];
						ind2++;
					}
				}
			}
			return static_cast<double>(tmp);
		}
		else {
			while ((ind1 + ind2) <= (len1 + len2) / 2) {
				if (ind1 == len1) {
					tmp1 = tmp;
					tmp = nums2[ind2];
					ind2++;
				}
				else if (ind2 == len2) {
					tmp1 = tmp;
					tmp = nums1[ind1];
					ind1++;
				}
				else {
					if (nums1[ind1] <= nums2[ind2]) {
						tmp1 = tmp;
						tmp = nums1[ind1];
						ind1++;
					}
					else {
						tmp1 = tmp;
						tmp = nums2[ind2];
						ind2++;
					}
				}
			}
			return static_cast<double>(tmp + tmp1)/2;
		}

	}
};