# LeetCode Solution
# Zeyu Liu
# 2019.2.26
# 292.Nim Game

from typing import List
# method 1 数学，因为自己可以拿1~3枚，每次自己拿完后剩4的倍数就可以赢，因此只要n不是4的倍数，都可以赢
class Solution:
    def canWinNim(self, n: int) -> bool:
    	return n % 4 != 0
# transfer method
solve = Solution()
print(solve.canWinNim(4))

# method 1 数学，利用位运算&
class Solution:
    def canWinNim(self, n: int) -> bool:
    	return n & 3 != 0
# transfer method
solve = Solution()
print(solve.canWinNim(4))