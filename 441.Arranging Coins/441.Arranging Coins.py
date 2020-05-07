# LeetCode Solution
# Zeyu Liu
# 2019.3.20
# 441.Arranging Coins

from typing import List
# method 1 iteration,较慢
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        s = 0
        for i in range(1,n+1):
            s += i
            if s > n:
                return i - 1
# transfer method
solve = Solution()
print(solve.arrangeCoins(8))

# method 2 math，等差数列求和公式, 慢
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        for i in range(1,n+1):
            if (1+i)*i/2 > n:
                return i - 1
# transfer method
solve = Solution()
print(solve.arrangeCoins(8))

# method 3 math, 最快, (1 + k) * k/ 2 = n, k^2 + k - 2 * n = 0, k = (-b + sqrt(b^2 - 4ac))/2a
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8*n) ** 0.5) // 2)
# transfer method
solve = Solution()
print(solve.arrangeCoins(8))

# method 4 binary research, 较快
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        h = n + 1 #重点1
        while l < h:
            mid = (l + h) // 2
            s = mid * (1 + mid) // 2
            if s <= n:
                l = mid + 1 #重点2
            else:
                h = mid
        return l - 1
# transfer method
solve = Solution()
print(solve.arrangeCoins(8))