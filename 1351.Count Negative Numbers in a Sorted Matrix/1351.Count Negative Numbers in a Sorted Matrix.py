# LeetCode Solution
# Zeyu Liu
# 2019.2.21
# 1351.Count Negative Numbers in a Sorted Matrix

from typing import List
# method 1 直接遍历DFS，O(n^2)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
    	count = 0
    	for i in grid:
    		for j in i:
    			if j < 0:
    				count += 1
    	return count
# transfer method
solve = Solution()
print(solve.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

# method 2 O(m+n)，利用已经按从大到小排序后的数组性质，注意elif意义
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(grid) and j < len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0])-j
                i += 1
                j = 0 
            elif j == len(grid[0])-1:
                i += 1
                j = 0 
            else:
                j +=1
        return(count)
# transfer method
solve = Solution()
print(solve.countNegatives([[5,1,0],[-5,-5,-5]]))

# method 3 O(mlogn) binary search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            start, end = 0, len(row)
            while start < end:
                mid = start +(end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(row)- start
        
        count = 0
        for row in grid:
            count += bin(row)
        return(count)
# transfer method
solve = Solution()
print(solve.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))