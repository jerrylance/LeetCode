# Leetcolode Solution
# Zeyu Liu
# 2019.5.21
# 661.Image Smoother

from typing import List
# method 1 matrix，根据题意，讨论所有情况，代码最多，但是最快
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m = len(M)
        n = len(M[0])
        matrix = [[0]*n for i in range(m)]
        # if m or n = 1
        if m == 1 and n == 1:
        	return M
        if m == 1:
        	matrix[0][0] = (M[0][0] + M[0][1]) // 2
        	matrix[0][-1] = (M[0][-2] + M[0][-1]) // 2
        	for i in range(1,n-1):
        		matrix[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1]) // 3
        	return matrix
        if n == 1:
        	matrix[0][0] = (M[0][0] + M[1][0]) // 2
        	matrix[-1][0] = (M[-2][0] + M[-1][0]) // 2
        	for i in range(1,m-1):
        		matrix[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0]) // 3
        	return matrix
        # 1 4 outside point
        matrix[0][0] = (M[0][0] + M[0][1] + M[1][0] + M[1][1]) // 4
        matrix[0][-1] = (M[0][-2] + M[0][-1] + M[1][-1] + M[1][-2]) // 4
        matrix[-1][0] = (M[-2][0] + M[-1][0] + M[-1][1] + M[-2][1]) // 4
        matrix[-1][-1] = (M[-2][-2] + M[-2][-1] + M[-1][-2] + M[-1][-1]) // 4
        # 2 4 merges points
        for i in range(1,m-1):
        	matrix[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0] + M[i-1][1] + M[i][1] + M[i+1][1]) // 6
        	matrix[i][-1] = (M[i-1][-1] + M[i][-1] + M[i+1][-1] + M[i-1][-2] + M[i][-2] + M[i+1][-2]) // 6  	
        for j in range(1,n-1):
        	matrix[0][j] = (M[0][j-1] + M[0][j] + M[0][j+1] + M[1][j-1] + M[1][j] + M[1][j+1]) // 6
        	matrix[-1][j] = (M[-1][j-1] + M[-1][j] + M[-1][j+1] + M[-2][j-1] + M[-2][j] + M[-2][j+1]) // 6
        # 3 inside point
        for i in range(1,m-1):
        	for j in range(1,n-1):
        		matrix[i][j] = (M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] + M[i][j-1] + M[i][j] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]) // 9
        return matrix
# transfer method
solve = Solution()
print(solve.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]

# method 2 设置方向dirs，记录满足计算条件的temp矩阵
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row, col = len(M), len(M[0])
        res = [[0]*col for i in range(row)]
        dirs = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        for i in range(row):
            for j in range(col):
                temp = [M[i+m][j+n] for m,n in dirs if 0<=i+m<row and 0<=j+n<col]
                res[i][j] = sum(temp)//len(temp)
        return res
# transfer method
solve = Solution()
print(solve.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))

# method 3 方法2的常规写法
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row, col = len(M), len(M[0])
        res = [[0] * col for i in M]
        for r in range(row):
            for c in range(col):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < row and 0 <= nc < col:
                            res[r][c] += M[nr][nc]
                            count += 1
                res[r][c] //= count
        return res
# transfer method
solve = Solution()
print(solve.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))