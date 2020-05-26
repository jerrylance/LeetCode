# LeetCode Solution
# Zeyu Liu
# 2019.4.26
# 997.Find the Town Judge

from typing import List
# method 1 straght forward, 慢
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        for i in range(1,N+1):
        	count = 0
        	for j in trust:
        		if j[0] == i:
        			count = 0
        			break
        		elif j[1] == i:
        			count += 1
        	if count == N-1:
        		return i
        return -1
# transfer method
solve = Solution()
print(solve.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))

# method 2 blowing mind, 计数，当被别人相信时次数+1，当相信别人时次数-1，快
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
    	count = [0] * (N+1)
    	for i,j in trust:
    		count[i] -= 1
    		count[j] += 1
    	for i in range(1,N+1):
    		if count[i] == N-1:
    			return i
    	return -1
# transfer method
solve = Solution()
print(solve.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))