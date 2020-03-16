# LeetCode Solution
# Zeyu Liu
# 2019.3.7
# 509.Fibonacci Number

from typing import List
# method 1 迭代法
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        f = [0] * (N+1)
        f[0] = 0
        f[1] = 1
        for i in range(2,N+1):
            f[i] = f[i-1] + f[i-2]
        return f[N]
# transfer method
solve = Solution()
print(solve.fib(20))

# method 2 方法1简化
class Solution:
    def fib(self, N: int) -> int:
        f0, f1 = 0, 1
        for i in range(N):
            f0, f1 = f1, f0 + f1
        return f0
# transfer method
solve = Solution()
print(solve.fib(20))

# method 3 math, 黄金分割
class Solution:
    def fib(self, N: int) -> int:
        golden_ratio = (1 + 5 ** 0.5)/2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)
# transfer method
solve = Solution()
print(solve.fib(20))

# method 4 递归, 极慢
class Solution:
    def fib(self, N: int) -> int:
        if N < 2: 
            return N
        else: 
            return self.fib(N-1) + self.fib(N-2)
# transfer method
solve = Solution()
print(solve.fib(20))