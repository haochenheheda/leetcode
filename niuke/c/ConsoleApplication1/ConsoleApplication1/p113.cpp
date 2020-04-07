#include "pch.h"
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

void s113() {
	int n;
	scanf_s("%d", &n);
	vector<int>num;
	unordered_map<int, int> mp;
	unordered_map<int, int> tmp_mp;
	for (int i = 0; i < n; ++i)
	{
		int tmp;
		scanf_s("%d", &tmp);
		num.push_back(tmp);
		mp[tmp] = 1;
	}
	int l = 0;
	int r = 0;
	for (r; r < num.size(); r++) {

		if (tmp_mp.find(num[r]) == tmp_mp.end()) tmp_mp[num[r]] = 1;
		else tmp_mp[num[r]] += 1;
		mp.erase(num[r]);
		if (mp.size() == 0) {break;}
	}
	int min_len = r-l;
	int r_ = r;
	vector<int> l_lst;
	vector<int> r_lst;

	for (r; r < num.size(); r++) {
		if (r != r_) tmp_mp[num[r]] += 1;
		while (1) {
			if (tmp_mp[num[l]] > 1) {
				tmp_mp[num[l]] -= 1;
				l += 1;
			}
			else break;
		}
		if (((r - l) == min_len)) {
			l_lst.push_back(l+1);
			r_lst.push_back(r+1);
		}
		else if ((r - l) < min_len) {
			min_len = r - l;
			l_lst.clear();
			l_lst.push_back(l+1);
			r_lst.clear();
			r_lst.push_back(r+1);

		}
	}
	printf("%d %d\n", min_len+1, l_lst.size());
	for (int i=0; i < l_lst.size(); i++) {
		if (i < l_lst.size() - 1) printf("[%d,%d] ",l_lst[i],r_lst[i]);
		else printf("[%d,%d]\n", l_lst[i], r_lst[i]);
	}

	return;
}
