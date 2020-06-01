# LeetCode Solution
# Zeyu Liu
# 2019.5.1
# 747.Largest Number At Least Twice of Others

from typing import List
# method 1 排序比较最大两个数
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
        	return 0
        n = sorted(nums)
        if n[-2] * 2 <= n[-1]:
        	return nums.index(n[-1])
        return -1
# transfer method
solve = Solution()
print(solve.dominantIndex([3, 6, 1, 0]))

# method 2 不用排序，直接遍历
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
        	return 0
        maxn = max(nums)
        index = nums.index(maxn)
        for i in nums:
        	if i != maxn and i * 2 > maxn:
        		return -1
        return index
# transfer method
solve = Solution()
print(solve.dominantIndex([3, 6, 1, 0]))

# method 3 O(n)，更新迭代最大两个数，线性赋值，最快
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
    	max1 = 0
    	max2 = 0
    	for i in nums:
    		if i > max1:
    			max2 = max1
    			max1 = i
    		elif i > max2:
    			max2 = i
    	if max1 >= max2 * 2:
    		return nums.index(max1)
    	return -1
# transfer method
solve = Solution()
print(solve.dominantIndex([3, 6, 1, 0]))