# LeetCode Solution
# Zeyu Liu
# 2019.3.13
# 12.Integer to Roman

from typing import List
# method 1 构建一个合适的字典dic,倒序，考虑9，4情况, while循环输出重复出现字符,快
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        n = ''
        for i in dic:
            while num >= i:
                n += dic[i]
                num -= i
        return n
# transfer method
solve = Solution()
print(solve.intToRoman(1994))

# method 2 一种巧妙的方法，快
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10];
# transfer method
solve = Solution()
print(solve.intToRoman(1994))