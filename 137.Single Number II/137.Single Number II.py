# LeetCode Solution
# Zeyu Liu
# 2019.2.26
# 137.Single Number II

from typing import List
# method 1 count(),慢
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

# transfer method
solve = Solution()
print(solve.singleNumber([2,2,3,2]))

# method 2 数学方法,快
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2

# transfer method
solve = Solution()
print(solve.singleNumber([2,2,3,2]))

# method 3 利用字典性质，较快，正常解法
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == 1:
                return i
        
# transfer method
solve = Solution()
print(solve.singleNumber([2,2,3,2]))
