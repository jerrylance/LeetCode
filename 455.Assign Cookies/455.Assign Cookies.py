# LeetCode Solution
# Zeyu Liu
# 2019.3.27
# 455.Assign Cookies

from typing import List
# method 1 greedy algorithm贪心算法，用最小的饼干开始，来判断是否满足需求最少的孩子,慢
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        child = 0
        for i in range(len(g)):
        	for j in range(len(s)):
        		if g[i] <= s[j]:
        			child += 1
        			s.pop(j)
        			break
        return child
# transfer method
solve = Solution()
print(solve.findContentChildren([1,2], [1,2,3]))

# method 1 greedy algorithm贪心算法，代码优化，快
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
    	g.sort()
    	s.sort()
    	child = 0
    	cookies = 0
    	while child < len(g) and cookies < len(s):
    		if g[child] <= s[cookies]:
    			child += 1
    		cookies += 1
    	return child
# transfer method
solve = Solution()
print(solve.findContentChildren([1,2], [1,2,3]))


