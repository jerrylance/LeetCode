# LeetCode Solution
# Zeyu Liu
# 2019.4.3
# 771.Jewels and Stones

from typing import List
# method 1 常规法
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
        	if i in J:
        		count += 1
        return count
# transfer method
solve = Solution()
print(solve.numJewelsInStones("aA", "aAAbbbb"))

# method 2 count()
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	count = 0
    	for i in J:
    		count += S.count(i)
    	return count
# transfer method
solve = Solution()
print(solve.numJewelsInStones("aA", "aAAbbbb"))

# method 3 Oneline
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(J.count,S))
# transfer method
solve = Solution()
print(solve.numJewelsInStones("aA", "aAAbbbb"))