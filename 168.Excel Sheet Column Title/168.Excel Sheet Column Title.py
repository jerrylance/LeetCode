# LeetCode Solution
# Zeyu Liu
# 2019.4.12
# 168.Excel Sheet Column Title

from typing import List
# method 1 字典法，chr()
class Solution:
    def convertToTitle(self, n: int) -> str:
        dic = {}
        for i in range(1,26):
        	dic[i] = chr(64 + i)
        s = ''
        dic[0] = 'Z'
        while n > 0:
        	s += dic[n%26]
        	n = (n-1) // 26 # 易错点(n-1)
        return s[::-1]
# transfer method
solve = Solution()
print(solve.convertToTitle(701))

# method 2 不用字典, ord(), chr(), 快
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:
            n -= 1
            s += chr(ord('A') + (n % 26))
            n //= 26
        return s[::-1]
# transfer method
solve = Solution()
print(solve.convertToTitle(701))

# method 3 方法2的列表形式解法
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = []      
        while n:
            s.append(chr(ord('A') + (n - 1) % 26))
            n = (n - 1) // 26            
        return ''.join(s[::-1])
# transfer method
solve = Solution()
print(solve.convertToTitle(701))