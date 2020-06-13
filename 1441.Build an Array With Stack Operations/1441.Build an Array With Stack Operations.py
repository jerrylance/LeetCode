# LeetCode Solution
# Zeyu Liu
# 2019.5.13
# 1441.Build an Array With Stack Operations

from typing import List
# method 1 基本列表操作
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
        	if i in target:
        		res.append('Push')
        	elif i not in target and i <= target[-1]:
        		res.append('Push')
        		res.append('Pop')
        return res
# transfer method
solve = Solution()
print(solve.buildArray([1,2], 4))

# method 2 方法1优化
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(1,target[-1]+1):
        	res.append('Push')
        	if i not in target:
        		res.append('Pop')
        return res
# transfer method
solve = Solution()
print(solve.buildArray([1,2], 4))
