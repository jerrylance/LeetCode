# LeetCode Solution
# Zeyu Liu
# 2019.1.24
# 13.Roman to Integer

from typing import List

# method 1 利用字典性质，前一个数小于第二个数时，算作负值，否则为正，
# 这里需要注意的是，字符串遍历不要超出范围
class Solution:
    def romanToInt(self, s: str) -> int:
        nums = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s) == 1:
            return dic[s[0]]
        else:
            for i in range(len(s)-1):
                if dic[s[i]] < dic[s[i+1]]:
                    nums -= dic[s[i]]
                else:
                     nums += dic[s[i]]
            return nums + dic[s[i+1]]
# transfer method
solve = Solution()
print(solve.romanToInt("D"))

# method 2 代码行数较少的方法，逆序相加和判断，速度比 method 1 慢一点
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res

# transfer method
solve = Solution()
print(solve.romanToInt("MCMXCIV"))

# method 3 方法1的思路来源，参考自其他大佬，速度比 method 2 慢一点
class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:          # rev the s
            if dict[i] >= prev:
                res += dict[i]     # sum the value iff previous value same or more
            else:
                res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
            prev = dict[i]
        return res
# transfer method
solve = Solution()
print(solve.romanToInt("MCMXCIV"))