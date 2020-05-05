# LeetCode Solution
# Zeyu Liu
# 2019.4.6
# 463.Island Perimeter

from typing import List
# method 1 straight forward，判断每个方格的左上两个位置是否为1，记录连接数*2,最快
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        area = 0
        connect = 0
        for row in range(len(grid)):
        	for col in range(len(grid[0])):
        		if grid[row][col] == 1:
        			area += 1
        			# 这里注意边界条件 row-1 >= 0, col-1 >= 0
        			if grid[row-1][col] == 1 and row > 0:
        				connect += 1
        			if grid[row][col-1] == 1 and col > 0:
        				connect += 1
        return area * 4 - connect * 2
# transfer method
solve = Solution()
print(solve.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))

# method 2 straight forward, 同方法1思想，记录位置值为1的边缘数, 较快
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        edge = 0
        for row in range(len(grid)):
        	for col in range(len(grid[0])):
        		if grid[row][col] == 1:
        			if row == 0 or grid[row-1][col] == 0:
        				edge += 1
        			if row == len(grid)-1 or grid[row+1][col] == 0:
        				edge += 1
        			if col == 0 or grid[row][col-1] == 0:
        				edge += 1
        			if col == len(grid[0])-1 or grid[row][col+1] == 0:
        				edge += 1
        return edge
# transfer method
solve = Solution()
print(solve.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))