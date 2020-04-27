# LeetCode Solution
# Zeyu Liu
# 2019.4.2
# 657.Robot Return to Origin

from typing import List
# method 1 count(), 快
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
        	return True
        else:
        	return False
# transfer method
solve = Solution()
print(solve.judgeCircle("UD"))

# method 2 常规法
class Solution:
    def judgeCircle(self, moves: str) -> bool:
    	row = 0
    	column = 0
    	for i in moves:
    		if i == 'L':
    			row += 1
    		elif i == 'R':
    			row -= 1
    		elif i == 'U':
    			column += 1
    		elif i == 'D':
    			column -= 1
    	return row == column == 0
# transfer method
solve = Solution()
print(solve.judgeCircle("UD"))

# method 3 Simulate movements
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        offsets = {"U":[0,1], "D":[0,-1], "R":[1,0], "L":[-1,0]}
        for move in moves:
            x,y = x+offsets[move][0], y+offsets[move][1]
        return (x == 0) and (y == 0)
# transfer method
solve = Solution()
print(solve.judgeCircle("UD"))