# LeetCode Solution
# Zeyu Liu
# 2019.2.17
# 70.Climbing Stairs

from typing import List
# method 1 动态规划，前面两项之和。
class Solution:
    def climbStairs(self, n: int) -> int:
        s = list(range(n+1))
        s[0] = 1
        s[1] = 1
        if n >= 2:
            for i in range(2,n+1):
                s[i] = s[i-1] + s[i-2]
            return s[n]
        else:
        	return n
# transfer method
solve = Solution()
print(solve.climbStairs(5))

# method 2 利用函数计算
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()
        return self.recur(n, dp)
        
    def recur(self, n, dp):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if dp.get(n):
            return dp[n]
        dp[n] = self.recur(n-1, dp) + self.recur(n-2, dp)
        return dp[n]   
# transfer method
solve = Solution()
print(solve.climbStairs(5))