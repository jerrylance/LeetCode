# LeetCode Solution
# Zeyu Liu
# 2019.4.27
# 1422.Maximum Score After Splitting a String

from typing import List
# method 1 切片，count()
class Solution:
    def maxScore(self, s: str) -> int:
        maxs = 0
        for i in range(1,len(s)):
        	score = s[:i].count('0') + s[i:].count('1')
        	maxs = max(maxs, score)
        return maxs
# transfer method
solve = Solution()
print(solve.maxScore("011101"))

# method 2 利用数学关系，求左边0-1最大情况，最后补上上全部1，快
class Solution:
    def maxScore(self, s: str) -> int:
    	zeros = 0
    	ones = 0
    	maxs = float('-inf')
    	for i,num in enumerate(s):
    		if num == '0':
    			zeros += 1
    		else:
    			ones += 1
    		if i != len(s) - 1:
    			maxs = max(maxs, zeros-ones)
    	return maxs + ones
# transfer method
solve = Solution()
print(solve.maxScore("1111"))