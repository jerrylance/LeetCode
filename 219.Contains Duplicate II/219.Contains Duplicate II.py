# LeetCode Solution
# Zeyu Liu
# 2019.2.14
# 219.Contains Duplicate II

from typing import List
# method 1 暴力枚举，超时
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    	for j in range(1,k+1):
    		for i in range(len(nums)-j):
    			if nums[i] == nums[i+j]:
    				return True
    	return False
# transfer method
solve = Solution()
print(solve.containsNearbyDuplicate([1,2,3,1,2,3],2))

# method 2 集合和切片概念，速度最快，切片索引超出索引范围不报错，可以继续迭代。但是如果单个对象下标超过范围，会报错。
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+1+k]:
                return True
        return False
# transfer method
solve = Solution()
print(solve.containsNearbyDuplicate([1,2,3,4,5,6,7,8,99,99],2))

# method 3 dictionary solution, enumerate()
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    	dic = {}
    	for i,num in enumerate(nums):
    		if num in dic and k >= i-dic[num]:
    			return True
    		else:
    			dic[num] = i
    	return False
# transfer method
solve = Solution()
print(solve.containsNearbyDuplicate([1,2],2))