# LeetCode Solution
# Zeyu Liu
# 2019.2.3
# 35.Search Insert Position
from typing import List

# method 1 普通解法遍历插入
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	if target in nums:
    		return nums.index(target)
    	else:
    		for i, num in enumerate(nums):
    			if num < target:
    				i += 1
    			else:
    				return i
    		return i
# transfer method    
solve = Solution()
print(solve.searchInsert([0],0))

# method 2 二分类查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	left = 0
    	right = len(nums) - 1
    	while left <= right:
    		mid = (left + right) // 2
    		if target == nums[mid]:
    			return mid
    		elif target > nums[mid]:
    			left = mid + 1
    		else:
    			right = mid -1
    	return left

# transfer method    
solve = Solution()
print(solve.searchInsert([1,3,4,5,6],7))

# method 3 排序
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	n = sorted(nums+[target])
    	return n.index(target)
# transfer method    
solve = Solution()
print(solve.searchInsert([1,3,4,5,6],7))

# method 4 bisect api二分查找模块
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	import bisect
    	return bisect.bisect_left(nums, target)
# transfer method    
solve = Solution()
print(solve.searchInsert([1,3,4,5,6],7))
