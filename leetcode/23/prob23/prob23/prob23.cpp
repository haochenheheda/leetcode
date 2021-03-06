// prob23.cpp : This file contains the 'main' function. Program execution begins and ends there.
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
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		int l = 0;
		int r = lists.size() - 1;
		return mergeLists(lists, l, r);
	}
private:
	ListNode* mergeLists(vector<ListNode*>& lists,int l,int r) {
		if (l > r) return nullptr;
		if (l == r) return lists[l];
		int m = (l + r) / 2;
		ListNode* l1 = mergeLists(lists, l, m);
		ListNode* l2 = mergeLists(lists, m+1, r);
		return merge(l1, l2);

	}
	ListNode* merge(ListNode* l1, ListNode* l2) {
		ListNode* head = new ListNode(0);
		ListNode* tmp = head;
		while (l1 != nullptr && l2 != nullptr) {
			if (l1->val < l2->val) {
				tmp->next = l1;
				tmp = tmp->next;
				l1 = l1->next;
			}
			else {
				tmp->next = l2;
				tmp = tmp->next;
				l2 = l2->next;
			}
		}
		if (l1 != nullptr) tmp->next = l1;
		if (l2 != nullptr) tmp->next = l2;
		return head->next;
	}
};
int main()
{
	Solution s;
	ListNode* h1 = new ListNode(1);
	h1->next = new ListNode(4);
	h1->next->next = new ListNode(5);

	ListNode* h2 = new ListNode(1);
	h2->next = new ListNode(3);
	h2->next->next = new ListNode(4);

	ListNode* h3 = new ListNode(2);
	h3->next = new ListNode(6);
	vector<ListNode*> lists;
	lists.push_back(h1);
	lists.push_back(h2);
	lists.push_back(h3);
	ListNode* r = s.mergeKLists(lists);
	while (r != nullptr) {
		printf("%d", r->val);
		r = r->next;
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
