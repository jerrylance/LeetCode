# LeetCode Solution
# Zeyu Liu
# 2019.1.20
# 268.Missing Number

from typing import List
# method 1 先排序，再找出相邻两个相差为2的数，中间一个就是missing值,考虑一些特殊情况后，可写出
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    	nums.sort()
    	for i, num in enumerate(nums):
        	if nums[i]-nums[i-1] == 2:
        		return(nums[i]-1)
        	elif i == len(nums)-1 and nums[0] != 0:
        		return(nums[0]-1)
        	elif i == len(nums)-1 and nums[0] == 0:
        		return(nums[-1]+1)
# transfer method
solve = Solution()
print(solve.missingNumber([1,3,4,2]))

# method 2 等差数列求和公式, 这个方法也有些问题，默认了数列从1开始
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    	theory_sum = ((1+len(nums)) * len(nums)) // 2
    	actual_sum = sum(nums)
    	return theory_sum - actual_sum
# transfer method
solve = Solution()
print(solve.missingNumber([1,3,4,2]))


# method 3 hashset 这个方法有点问题，不适用于类似[8,9]情况
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# transfer method
solve = Solution()
print(solve.missingNumber([1,3,4,2]))

