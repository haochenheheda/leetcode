#coding:utf-8
nums = [3,2,4]
target = 6
def solution1(nums,target):
	for i in range(len(nums)-1):
		for j in range(i+1,len(nums)):
			if nums[i] + nums[j] == target:
				return [i,j]

def solution2(nums,target):
	map_ = {}
	for i,num in enumerate(nums):
		map_[target - num] = i

	for i,num in enumerate(nums):
		if map_.has_key(num):#python3 不支持has_key 但是用 k in map.keys()判断，时间复杂度是O(n),而用has_key判断，时间复杂度是O(1)
			if i != map_[num]:
				return [i,map_[num]]

def solution3(nums,target):
	map_ = {}
	for i,num in enumerate(nums):
		if map_.has_key(num):
			return [map_[num],i]
		map_[target - num] = i	
if __name__ == '__main__':
	print(solution3(nums,target))