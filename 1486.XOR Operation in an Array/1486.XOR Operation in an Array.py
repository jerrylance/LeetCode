# LeetCode Solution
# Zeyu Liu
# 2019.6.22
# 1486.XOR Operation in an Array

from typing import List
# method 1 ^位运算
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        XOR = 0
        for i in range(n):
        	nums[i] = start + 2*i
        	XOR ^= nums[i]
        return XOR
# transfer method
solve = Solution()
print(solve.xorOperation(4, 3))

# method 2 方法1优化
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        out = start
        for i in range(1, n):
            out ^= start + 2 * i
        return out
# transfer method
solve = Solution()
print(solve.xorOperation(4, 3))

# method 3 O(1)time, math，找规律
class Solution:
    def xorOperation(self, n: int, start: int) -> int:       
        last = start + 2 * (n - 1)        
        if start % 4 <= 1:
            ans = [0, last, 2, last^2]
            return ans[n % 4]      
        else: 
            ans = [start ^ last ^ 2, start, start ^ last, start ^ 2]
            return ans[n % 4]
# transfer method
solve = Solution()
print(solve.xorOperation(4, 3))