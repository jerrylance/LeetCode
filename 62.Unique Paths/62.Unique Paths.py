# LeetCode Solution
# Zeyu Liu
# 2019.3.1
# 62.Unique Paths

from typing import List
# method 1 dynamic programming动态规划，重要例题,最后到达位置走法是上面和左边两个之和。这里需要注意的是dp取值范围。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
# 另一种写法,比较好懂
#        dp = [[0] * m] * n
#        for i in range(n):
#            for j in range(m):
#                if i == 0 or j == 0:
#                    dp[i][j] = 1
#                else:
#                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
#        return dp[-1][-1]
    '''
    动态规划
    1： 状态定义： dp[i][j]  到了[i,j] 位置， 存在可能的路径 
    2： 状态转移方程： dp[i][j] = dp[i][j-1] + dp[i-1][j]
    '''
# transfer method
solve = Solution()
print(solve.uniquePaths(7,3))

# method 2 数学法，C(m-1+n-1,m-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m1 = 1
        for i in range(1,m):
            m1 = m1*i
        n1 = 1
        for i in range(1,n):
            n1 = n1*i
        mn = 1
        for i in range(1,m+n-1):
            mn = mn*i
        return mn//(m1*n1)
        # 或者直接调用math函数
        #from math import factorial
        #return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
# transfer method
solve = Solution()
print(solve.uniquePaths(7,3))

# method 3 O(n) space 不好理解
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                cur[j] += cur[j-1]
        return cur
        return cur[-1]
# transfer method
solve = Solution()
print(solve.uniquePaths(7,3))