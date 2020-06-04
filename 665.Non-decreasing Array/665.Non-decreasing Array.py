# LeetCode Solution
# Zeyu Liu
# 2019.5.4
# 665.Non-decreasing Array

from typing import List
# method 1 float('-inf')，最快
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
        	return True
        count = 0
        nums = [float('-inf')] + nums + [float('inf')]
        for i in range(1, len(nums)-1):
        	if nums[i] > nums[i+1]:
        		count += 1
        		index = i
        		if count > 1:
        			return False
        if count == 0:
        	return True
        if count == 1 and nums[index-1] <= nums[index+1]:
        	return True
        if count == 1 and nums[index] <= nums[index+2]:
        	return True
        return False
# transfer method
solve = Solution()
print(solve.checkPossibility([3,4,2,3]))

# method 2 不是很好想的思路
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if modified:
                    return False
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                modified = True
        return True
# transfer method
solve = Solution()
print(solve.checkPossibility([3,4,2,3]))