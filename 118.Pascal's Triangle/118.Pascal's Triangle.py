# LeetCode Solution
# Zeyu Liu
# 2019.5.11
# 118.Pascal's Triangle

from typing import List
# method 1 straight forward，常规法
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
        	return [[1]]
        N = [0] * numRows
        N[0] = [1]
        N[1] = [1,1]
        for i in range(2, numRows):
        	N[i] = [1] + [N[i-1][j] + N[i-1][j+1] for j in range(len(N[i-1])-1)] + [1]
        return N
# transfer method
solve = Solution()
print(solve.generate(5))

# method 2 方法1优化,快
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    	pascal = [[1]*(i+1) for i in range(numRows)]
    	for i in range(numRows):
    		for j in range(1,i):
    			pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    	return pascal
# transfer method
solve = Solution()
print(solve.generate(5))