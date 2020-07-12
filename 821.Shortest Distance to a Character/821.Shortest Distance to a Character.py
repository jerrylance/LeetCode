# LeetCode Solution
# Zeyu Liu
# 2019.5.24
# 821.Shortest Distance to a Character

from typing import List
# method 1 two pass分别向右和向左遍历，查找最小距离，快
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = [len(S)] * len(S)
        count = len(S)
        for i in range(len(S)):
        	if S[i] == C:
        		res[i] = 0
        		count = 0
        	else:
        		count += 1
        		res[i] = count
        count = len(S)
        for i in range(len(S)-1,-1,-1):
        	if S[i] == C:
        		res[i] = 0
        		count = 0
        	else:
        		count += 1
        		res[i] = min(count,res[i])
        return(res)
# transfer method
solve = Solution()
print(solve.shortestToChar("loveleetcode", 'e'))

# method 2 方法1优化, abs()
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = [len(S)] * len(S)
        pos = float('-inf')
        for i in list(range(len(S))) + list(range(len(S))[::-1]):
        	if S[i] == C:
        		pos = i
        	res[i] = min(res[i], abs(i - pos))
        return res
# transfer method
solve = Solution()
print(solve.shortestToChar("loveleetcode", 'e'))