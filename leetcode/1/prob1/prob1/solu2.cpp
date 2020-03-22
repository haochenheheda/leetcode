#include "pch.h"
#include <vector>
#include <map>
using namespace std;
vector<int> solution2(vector<int>& nums, int target)
{
	vector<int> result(2);
	map<int, int> map_;
	for (int i = 0; i < nums.size(); i++) {
		map_[target - nums[i]] = i;
		}
	for (int i = 0; i < nums.size(); i++) {
		if (map_.count(nums[i]) == 1 && map_[nums[i]] != i) {
			result[0] = i; result[1] = map_[nums[i]];
			return result;
		}
	}
	return result;
}
