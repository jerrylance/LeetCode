# LeetCode Solution
# Zeyu Liu
# 2019.4.5
# 53.Maximum Subarray

from typing import List
# method 1 append()列表操作
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        mid = sum(nums)//2
        num = []
        count = 0
        for i in sorted(nums)[::-1]:
        	num.append(i)
        	count += i
        	if count > mid:
        		return num
# transfer method
solve = Solution()
print(solve.minSubsequence([4,3,10,9,8]))

# method 2 pop()列表操作
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        mid = sum(nums)//2
        nums.sort()
        num = []
        count = 0
        while True:
        	x = nums.pop()
        	count += x
        	num.append(x)
        	if count > mid:
        		return num
# transfer method
solve = Solution()
print(solve.minSubsequence([4,3,10,9,8]))