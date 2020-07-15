# LeetCode Solution
# Zeyu Liu
# 2019.6.6
# 868.Binary Gap

from typing import List
# method 1 常规法,字符串操作，bin always start from "1'.
class Solution:
    def binaryGap(self, N: int) -> int:
        d = 0
        count = 0
        N = bin(N)
        for i in range(3, len(N)):
        	if N[i] == '1':
        		count += 1
        		d = max(d, count)
        		count = 0
        	else:
        		count += 1
        return d
# transfer method
solve = Solution()
print(solve.binaryGap(22))

# method 2 方法1优化
class Solution:
    def binaryGap(self, N: int) -> int:
        p = d = 0
        for i, num in enumerate(bin(N)[2:]):
            if num == "1":
                d= max(d, i - p)
                p = i
        return d
# transfer method
solve = Solution()
print(solve.binaryGap(22))