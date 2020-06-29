# LeetCode Solution
# Zeyu Liu
# 2019.5.16
# 566.Reshape the Matrix

from typing import List
# method 1 二维矩阵操作，注意矩阵初始化
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
        	return nums
        new = [[0]*c for i in range(r)] # 注意不能写成 new = [[0]*c]*r，显示一样，实际是不一样的
        m = 0
        n = 0
        for i in range(len(nums)):
        	for j in range(len(nums[0])):
        		new[m][n] = nums[i][j]
        		n += 1
        		if n == c:
        			m += 1
        			n = 0
        return new
# transfer method
solve = Solution()
print(solve.matrixReshape([[1,2],[3,4]],4,1))

# method 2 利用列表再排列
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
        	return nums
        l = []
        for i in nums:
            for j in i:
                l.append(j) # l 是初始矩阵顺序列表
        return [l[i:i+c] for i in range(0,len(l),c)]
# transfer method
solve = Solution()
print(solve.matrixReshape([[1,2],[3,4]],1,4))