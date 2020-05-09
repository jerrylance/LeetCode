# LeetCode Solution
# Zeyu Liu
# 2019.4.9
# 521.Longest Uncommon Subsequence I 

from typing import List
# method 1 阅读理解，比较简单
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
        	return -1
        return max(len(a),len(b))
# transfer method
solve = Solution()
print(solve.findLUSlength("aba", "cdc"))

# method 2 Oneline
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a),len(b))
# transfer method
solve = Solution()
print(solve.findLUSlength("aba", "cdc"))