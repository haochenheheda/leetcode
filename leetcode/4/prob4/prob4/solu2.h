#pragma once
#include <vector>
#include <iostream>
#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;
class Solution1 {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int len1 = nums1.size();
		int len2 = nums2.size();
		if (len1 > len2) {
			return findMedianSortedArrays(nums2, nums1);
		}
		int l = 0, r = len1;
		int ind1, ind2,max1,max2,min1,min2;
		int mid = (len1 + len2) / 2;
		while (1) {
			ind1 = (l + r) / 2;
			ind2 = mid - ind1;
			max1 = (ind1 == 0) ? INT_MIN : nums1[ind1 - 1];
			max2 = (ind2 == 0) ? INT_MIN : nums2[ind2 - 1];
			min1 = (ind1 == len1) ? INT_MAX : nums1[ind1];
			min2 = (ind2 == len2) ? INT_MAX : nums2[ind2];
			if (max1 > min2) {
				r = ind1;
			}
			else if (max2 > min1) {
				l = ind1 + 1;
			}
			else break;
		};
		if ((len1 + len2) % 2) {
			return min(min1, min2);
		}
		else {
			return static_cast<double>(min(min1, min2) + max(max1, max2)) / 2;
		}
	}
};