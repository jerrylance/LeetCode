# LeetCode Solution
# Zeyu Liu
# 2019.6.26
# 682.Baseball Game

from typing import List
# method 1 O(n)time, stack,list列表操作
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        sums = []
        for i in ops:
        	if i == 'C':
        		sums.pop()
        	elif i == 'D':
        		sums.append(2 * sums[-1])
        	elif i == '+':
        		sums.append(sums[-1] + sums[-2])
        	else:
        		sums.append(int(i))
        return sum(sums)
# transfer method
solve = Solution()
print(solve.calPoints(["5","-2","4","C","D","9","+","+"]))