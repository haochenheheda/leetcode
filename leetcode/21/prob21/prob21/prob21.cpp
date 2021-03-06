// prob21.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

 //Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		ListNode* head = new ListNode(0);
		ListNode* head_ = head;
		while (l1 != nullptr && l2 != nullptr) {
			if (l1->val < l2->val) {
				head_->next = l1;
				head_ = head_->next;
				l1 = l1->next;
			}
			else {
				head_->next = l2;
				head_ = head_->next;
				l2 = l2->next;
			}
		}
		if (l1 != nullptr) head_->next = l1;
		if (l2 != nullptr) head_->next = l2;
		return head->next;
	}
};
int main()
{
	ListNode l1 = ListNode(1);
	ListNode l12 = ListNode(2);
	ListNode l13 = ListNode(3);
	l1.next = &l12;
	l12.next = &l13;
	ListNode l2 = ListNode(1);
	ListNode l22 = ListNode(3);
	ListNode l23 = ListNode(4);
	l2.next = &l22;
	l22.next = &l23;
	Solution s;
	ListNode* re = s.mergeTwoLists(&l1, &l2);
	while (re != nullptr) {
		printf("%d", re->val);
		re = re->next;
	}
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
