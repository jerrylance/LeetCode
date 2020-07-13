# LeetCode Solution
# Zeyu Liu
# 2019.4.19
# 832.Flipping an Image

from typing import List
# method 1 straight forwar
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in A:
        	l = []
        	for j in i[::-1]:
        		if j == 1:
        			l.append(0)
        		else:
        			l.append(1)
        	res.append(l)
        return res
# transfer method
solve = Solution()
print(solve.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

# method 2 Oneline
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    	return [[1-j for j in i[::-1]] for i in A]
# transfer method
solve = Solution()
print(solve.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

# method 3 位运算，异或^
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    	for row in A:
    		i, j = 0, len(row) - 1
    		while i <= j:
    			if row[i] == row[j]:
    				row[i], row[j] = row[i]^1, row[j]^1
    			i += 1
    			j -= 1
    	return A
# transfer method
solve = Solution()
print(solve.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))