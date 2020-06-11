# LeetCode Solution
# Zeyu Liu
# 2019.5.11
# 119.Pascal's Triangle II

from typing import List
# method 1 straight forward, 遍历输出最后一个即可
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
        	return [1]
        N = [0] * (rowIndex+1)
        N[0] = [1]
        N[1] = [1,1]
        for i in range(1,rowIndex+1):
        	N[i] = [1] + [N[i-1][j] + N[i-1][j+1] for j in range(len(N[i-1])-1)] + [1]
        return N[-1]
# transfer method
solve = Solution()
print(solve.getRow(3))

# method 2 方法1优化, 更简洁
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	pascal = [[1]*(i+1) for i in range(rowIndex+1)]
    	for i in range(rowIndex+1):
    		for j in range(1,i):
    			pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    	return pascal[-1]
# transfer method
solve = Solution()
print(solve.getRow(3))