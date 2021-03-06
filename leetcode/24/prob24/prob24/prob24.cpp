// prob24.cpp : This file contains the 'main' function. Program execution begins and ends there.
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
	ListNode* swapPairs(ListNode* head) {
		ListNode* head_ = new ListNode(0);
		head_->next = head;
		ListNode* prev = head_;
		while (head != nullptr && head -> next != nullptr) {
			ListNode* t1 = head;
			ListNode* t2 = head->next;
			ListNode* nxt = t2->next;
			prev->next = t2;
			t2->next = t1;
			t1->next = nxt;
			head = nxt;
			prev = t1;
		}
		return head_->next;

	}
};
int main()
{
	Solution s;
	//s.swapPairs();
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
