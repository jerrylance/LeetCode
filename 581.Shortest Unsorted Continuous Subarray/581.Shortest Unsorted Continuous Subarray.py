# LeetCode Solution
# Zeyu Liu
# 2019.3.30
# 581.Shortest Unsorted Continuous Subarray

from typing import List
# method 1 先排序，正反各遍历一遍，如果和原数组值不一样，输出索引，+1相减,快
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        a = 0
        b = 0
        for i in range(len(nums1)):
        	if nums[i] != nums1[i]:
        		a = i
        		break
        for i in range(len(nums1)-1, 0, -1):
        	if nums[i] != nums1[i]:
        		b = i
        		break
        if a == b:
        	return 0
        return b+1-a
# transfer method
solve = Solution()
print(solve.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

# method 2 iteration
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
    	nums1 = sorted(nums)
    	if nums1 == nums:
    		return 0
    	start = 0
    	end = len(nums) - 1
    	while nums1[start] == nums[start]:
    		start += 1
    	while nums1[end] == nums[end]:
    		end -= 1
    	return end + 1 - start
# transfer method
solve = Solution()
print(solve.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

# method 3 利用enumerate,zip()，较慢
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
    	res = [i for (i,(a,b)) in enumerate(zip(nums,sorted(nums))) if a!=b]
    	if not res:
    		return 0 
    	else:
    		return res[-1]-res[0]+1
# transfer method
solve = Solution()
print(solve.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))