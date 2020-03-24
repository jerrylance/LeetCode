# LeetCode Solution
# Zeyu Liu
# 2019.3.10
# 342.Power of Four

from typing import List
# method 1 recursive
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num > 0:
            if num == 1:
                return True
            if num % 4 == 0:
                num = num // 4
            else:
                return False
        return False
# transfer method
solve = Solution()
print(solve.isPowerOfFour(16))

# method 2 数学性质
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        for i in range(int(num ** 1/4)+1):
            if 4 ** i == num:
                return True
            elif 4 ** i > num:
                return False
# transfer method
solve = Solution()
print(solve.isPowerOfFour(16))

# method 3 &位运算，满足二的阶乘同时满足二进制mask：0b01010101010101010101010101010101(1431655765)
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and num & 0b01010101010101010101010101010101 == num
# transfer method
solve = Solution()
print(solve.isPowerOfFour(16))

# method 4 位运算，优化
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s = bin(num)[3:] # 去掉首1
        return num!=0 and ('1' not in s) and len(s)%2 == 0
# transfer method
solve = Solution()
print(solve.isPowerOfFour(16))