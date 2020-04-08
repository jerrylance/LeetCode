# LeetCode Solution
# Zeyu Liu
# 2019.3.20
# 171.Excel Sheet Column Number

from typing import List
# method 1 字典法
class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
        'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        c = 0
        l = len(s)
        for i in s:
            c += dic[i]*(26**(l-1))
            l -= 1
        return c
# transfer method
solve = Solution()
print(solve.titleToNumber("ZY"))

# method 2 ord()，AC编码号，方法1优化
class Solution:
    def titleToNumber(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            c *= 26
            c += (ord(s[i]) - ord('A') + 1) 
        return c
# transfer method
solve = Solution()
print(solve.titleToNumber("ZY"))