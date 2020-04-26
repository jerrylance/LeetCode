# LeetCode Solution
# Zeyu Liu
# 2019.4.1
# 704.Binary Search

from typing import List
# method 1 binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
        	mid = (left + right) // 2
        	if nums[mid] == target:
        		return mid
        	elif nums[mid] > target:
        		right = mid - 1
        	elif nums[mid] < target:
        		left = mid + 1
        return -1
# transfer method
solve = Solution()
print(solve.search([-1,0,3,5,9,12],9))