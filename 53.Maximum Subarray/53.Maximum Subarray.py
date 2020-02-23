# LeetCode Solution
# Zeyu Liu
# 2019.2.21
# 53.Maximum Subarray

from typing import List
# method 1 暴力，超时
class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 1
        num = 0
        for i in range(1,n+1):
            s = s * i
        for i in str(s)[::-1]:
            if i == '0':
                num += 1
            else:
                return num
# transfer method
solve = Solution()
print(solve.trailingZeroes(30))

# method 2 递归，数学思考，阶乘末尾为0，只能是2*5，求2*5的个数,快
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        if n < 10:
            return 1
        return n//5 + self.trailingZeroes(n//5)
# transfer method
solve = Solution()
print(solve.trailingZeroes(30))

# method 3 数学思考，阶乘2比5多得多，求5的个数即可,注意25 = 5*5，125 = 5*5*5，最快
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        while n >= 5:
            n = n//5
            num += n
        return num
# transfer method
solve = Solution()
print(solve.trailingZeroes(30))