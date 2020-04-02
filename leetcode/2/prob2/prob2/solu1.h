#pragma once
#include <iostream>
using namespace std;
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {};

};
class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode *r = new ListNode(0);
		ListNode *t = r;
		int tmp = 0;
		while (l1 != NULL || l2 != NULL) {
			int x1 = 0;
			int x2 = 0;
			if (l1 != NULL) {
				x1 = l1->val;
				l1 = l1->next;
			}
			if (l2 != NULL) {
				x2 = l2->val;
				l2 = l2->next;
			}
			t->next = new ListNode((x1 + x2 + tmp) % 10);
			tmp = (x1 + x2 + tmp) / 10;
			t = t->next;
		}
		if (tmp != 0) t->next = new ListNode(tmp);
		return r->next;
	}
};