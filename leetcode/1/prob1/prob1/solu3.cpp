#include "pch.h"
#include <vector>
#include <map>
using namespace std;
vector<int> solution3(vector<int>& nums, int target)
{
	vector<int> result(2);
	map<int, int> map_;
	for (int i = 0; i < nums.size(); i++) {
		if (map_.count(nums[i]) == 1 && map_[nums[i]] != i) {
			result[1] = i; result[0] = map_[nums[i]];
			return result;
		}
		map_[target - nums[i]] = i;
	}
	return result;
}
