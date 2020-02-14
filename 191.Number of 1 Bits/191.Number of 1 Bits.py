# LeetCode Solution
# Zeyu Liu
# 2019.2.13
# 191.Number of 1 Bits

from typing import List
# method 1 bin()转成二进制，再转成字符串计算1的数量
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        return n.count('1')

# transfer method
solve = Solution()
print(solve.hammingWeight(5))

# method 2 人工转2进制
class Solution:
    def hammingWeight(self, n: int) -> int:
        a = ''
        while n > 0:
            a += str(n%2)
            n = n//2
        count = 0
        for i in a:
            if i == '1':
                count += 1
        return count

# transfer method
solve = Solution()
print(solve.hammingWeight(55))

# method 3 方法2优化
class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 0
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n//2
        return count

# transfer method
solve = Solution()
print(solve.hammingWeight(555))