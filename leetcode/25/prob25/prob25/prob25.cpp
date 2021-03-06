// prob25.cpp : This file contains the 'main' function. Program execution begins and ends there.
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
	ListNode* reverseKGroup(ListNode* head, int k) {
		if (k == 1) return head;
		int size = 0;
		ListNode* tmp = head;
		while (tmp != nullptr) { size++; tmp = tmp->next; }
		int t = size / k * k;
		ListNode* head_ = new ListNode(0);
		ListNode* prev = head_;
		head_->next = head;
		ListNode* p = head;
		ListNode* nxt_prev = new ListNode(0);
		ListNode* nxt = new ListNode(0);
		int t_ = 1;
		while (t_ <= t) {
			if (t_%k == 1) nxt_prev = p;
			nxt = p->next;
			ListNode* n = prev->next;
			prev->next = p;
			p->next = n;
			p = nxt;
			if (t_%k == 0) prev = nxt_prev;
			t_++;
		}
		prev->next = nxt;
		return head_->next;
	}
};
int main()
{
	Solution s;
	int k = 2;
	ListNode* head = new ListNode(1);
	head->next = new ListNode(2);
	head->next->next = new ListNode(3);
	head->next->next->next = new ListNode(4);
	head->next->next->next->next = new ListNode(5);
	s.reverseKGroup(head, k);
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
