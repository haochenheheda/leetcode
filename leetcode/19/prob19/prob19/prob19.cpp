// prob19.cpp : This file contains the 'main' function. Program execution begins and ends there.
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
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		ListNode p = ListNode(0);
		p.next = head;
		ListNode * tmp = &p;
		ListNode * p_ = &p;
		for (int i = 0; i < n+1; i++) {
			tmp = tmp->next;
		}
		while (tmp != nullptr) {
			tmp = tmp->next;
			p_ = p_->next;
		}
		p_->next = p_->next->next;
		return p.next;
	}
};
int main()
{
	Solution s;
    std::cout << "Hello World!\n"; 
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
