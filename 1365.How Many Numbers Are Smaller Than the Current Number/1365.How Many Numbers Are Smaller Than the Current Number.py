# LeetCode Solution
# Zeyu Liu
# 2019.4.8
# 1365.How Many Numbers Are Smaller Than the Current Number

from typing import List
# method 1 O(n^2)，暴力，较慢
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        res = []
        for i in nums:
        	for j in nums:
        		if i > j:
        			count += 1
        	res.append(count)
        	count = 0
        return res
# transfer method
solve = Solution()
print(solve.smallerNumbersThanCurrent([8,1,2,2,3]))

# method 2 字典法，发现返回值正好是排序后对应的系数,快
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    	dic = {}
    	for i, num in enumerate(sorted(nums)):
    		if num not in dic:
    			dic[num] = i
    	return [dic[num] for num in nums]
# transfer method
solve = Solution()
print(solve.smallerNumbersThanCurrent([8,1,2,2,3]))