# LeetCode Solution
# Zeyu Liu
# 2019.1.18
# 153. Find Minimum in Rotated Sorted Array
from typing import List
# method 1 我这个方法更容易想
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
        	return nums[0]
        else:
        	for i, num in enumerate(nums):
        		try:
        			if nums[i+1] < nums[i]:
        				return nums[i+1]
        		except:
        			return nums[0]
# transfer method
solve = Solution()
print(solve.findMin([4,5,6,1,2]))

# method 2 Binary Search(正统方法)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while nums[left] > nums[right]:
            middle  = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        return nums[left]
# transfer method
solve = Solution()
print(solve.findMin([4,5,6,1,2]))


# method 3 just a joke!
class Solution:
    def findMin(self, nums: List[int]) -> int:
    	return min(nums)
# transfer method
solve = Solution()
print(solve.findMin([4,5,6,1,2]))