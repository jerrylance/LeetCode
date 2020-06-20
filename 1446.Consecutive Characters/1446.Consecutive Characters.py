# LeetCode Solution
# Zeyu Liu
# 2019.5.17
# 1446.Consecutive Characters

from typing import List
# method 1 one pass, iteration
class Solution:
    def maxPower(self, s: str) -> int:
        length = 1
        maxlength = 1
        for i in range(len(s)-1):
        	if s[i] == s[i+1]:
        		length += 1
        	else:
        		length = 1
        	maxlength = max(length, maxlength)
        return maxlength
# transfer method
solve = Solution()
print(solve.maxPower("hooraaaaaaaaaaay"))

# method 2 API, Oneline
class Solution:
    def maxPower(self, s: str) -> int:
    	import itertools
    	return max(len(list(b)) for a, b in itertools.groupby(s))
# transfer method
solve = Solution()
print(solve.maxPower("hooraaaaaaaaaaay"))