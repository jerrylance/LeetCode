# LeetCode Solution
# Zeyu Liu
# 2019.3.8
# 1374.Generate a String With Characters That Have Odd Counts
from typing import List
# method 1 奇偶判定
class Solution:
    def generateTheString(self, n: int) -> str:
    	if n % 2 == 0:
    		return 'x'*(n-1)+'y'
    	else:
    		return 'x'*n
# transfer method
solve = Solution()
print(solve.generateTheString(4))