# LeetCode Solution
# Zeyu Liu
# 2019.7.30
# 1496.Path Crossing

from typing import List
# method 1 simulation, straight forward
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a, b = 0, 0
        points = []
        for i in path:
        	if i == 'N':
        		b += 1
        	elif i == 'S':
        		b -= 1
        	elif i == 'W':
        		a -= 1
        	elif i == 'E':
        		a += 1
        	if [a,b] in points or [a,b] == [0,0]:
        		return True
        	points.append([a,b])
        return False
# transfer method
solve = Solution()
print(solve.isPathCrossing("NES"))

# method 2 利用集合set，方法1优化
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a, b = 0, 0
        se = set()
        se.add((0,0))
        for p in path:
            if p == 'N':
                b += 1
            elif p == 'S':
                b -= 1
            elif p == 'E':
                a += 1
            elif p == 'W':
                a -= 1
            if (a,b) in se:
                return True
            se.add((a,b))
        return False
# transfer method
solve = Solution()
print(solve.isPathCrossing("NES"))