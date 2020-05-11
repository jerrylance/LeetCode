# LeetCode Solution
# Zeyu Liu
# 2019.4.10
# 867.Transpose Matrix

from typing import List
# method 1 转置矩阵操作，注意细节，这道题先遍历列再遍历行，否则若矩阵非方阵会导致系数溢出
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
    	A1 = []
    	for j in range(len(A[0])):
    		A2 = []
    		for i in range(len(A)):
    			A2.append(A[i][j])
    		A1.append(A2)
    	return A1
# transfer method
solve = Solution()
print(solve.transpose([[1,2,3],[4,5,6],[7,8,9]]))

# method 2 zip(*)求转置, 最快
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
    	return list(zip(*A))
# transfer method
solve = Solution()
print(solve.transpose([[1,2,3],[4,5,6],[7,8,9]]))

# method 3 Oneline, 方法1简洁写法
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
# transfer method
solve = Solution()
print(solve.transpose([[1,2,3],[4,5,6],[7,8,9]]))
