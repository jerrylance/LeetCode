# LeetCode Solution
# Zeyu Liu
# 2019.12.31
# 1.Two Sum

# method 1
# 暴力
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        renums = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    renums.append(i)
                    renums.append(j)
                    return(renums)
# transfer method
solve = Solution()
print(solve.twoSum([2,7,11,15],9))

# method 2
# 哈希(比较好)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	dictory = {}
    	for i, num in enumerate(nums):
    		if num in dictory:
    			return[dictory[num], i]
    		else:
    			dictory[target - num] = i
# enumerate()函数可以把一个List按照索引从小到大的顺序组成一个字典
# 速度最快
# transfer method
solve = Solution()
print(solve.twoSum([2,7,11,15],9))

# method 3
# 切片
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
        	if target - nums[i] in nums[i+1:]:
        		return [i, nums.index(target - nums[i],i+1)]
# 这里return中的i+1，是index函数中的参数，意味着索引起始值从自己下一个数开始，如果不设置，那么如果有相等value时，如(3,3),6这种情况下会返回[0,0]，而不是[0,1]
# 切片占用内存较小
# transfer method
solve = Solution()
print(solve.twoSum([2,7,11,15,-2],9))