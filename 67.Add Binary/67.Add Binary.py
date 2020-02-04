# LeetCode Solution
# Zeyu Liu
# 2019.2.1
# 67.Add Binary
from typing import List

# method 1 将字符串转化成整数求和，再转化成整数列表迭代
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = [int(x) for x in str(int(a) + int(b))]
        for i in range(1,len(s)):
            if s[-i] == 2:
                s[-i] = 0
                s[-(i+1)] += 1
            elif s[-i] == 3:
                s[-i] = 1
                s[-(i+1)] += 1
        if s[0] == 2:
            s[0] = 0
            s = [1] + s
        elif s[0] == 3:
            s[0] = 1
            s = [1] + s
        return "".join([str(x) for x in s])

# transfer method    
solve = Solution()
print(solve.addBinary("1111","11"))

# method 2 将二进制转化为十进制，bin() 返回一个整数 int 或者长整数 long int 的二进制表示(注意要作切片[2:])
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a,2), int(b,2)
        return bin(x+y)[2:]

# transfer method    
solve = Solution()
print(solve.addBinary("1111","11"))