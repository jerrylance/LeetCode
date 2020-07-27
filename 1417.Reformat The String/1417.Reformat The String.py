# LeetCode Solution
# Zeyu Liu
# 2019.6.25
# 1417.Reformat The String

from typing import List
# method 1 brute, list, isaplha()
class Solution:
    def reformat(self, s: str) -> str:
        char = []
        digit = []
        for i in s:
        	if i.isalpha():
        		char.append(i)
        	else:
        		digit.append(i)
        res = ''
        if abs(len(char) - len(digit)) <= 1:
        	if len(char) > len(digit):
        		for i in range(len(digit)):
        			res += char[i] + digit[i]
        		return res + char[-1]
        	elif len(char) < len(digit):
        		for i in range(len(char)):
        			res += digit[i] + char[i]
        		return res + digit[-1]
        	else:
        		for i in range(len(char)):
        			res += digit[i] + char[i]
        		return res
        return ""
# transfer method
solve = Solution()
print(solve.reformat("covid2019"))

# method 2 方法1优化
class Solution:
    def reformat(self, s: str) -> str:
        digits = '0123456789'
        p1 = []
        p2 = [] 
        result = []
        for char in s:
            if char in digits:
                p1.append(char)
            else:
                p2.append(char)
        if len(p1) < len(p2):
            p1 , p2 = p2, p1
        if len(p1) - len(p2) > 1:
            return ""
        #p1 is the longest one
        for i in range(len(p1) + len(p2)):
            if i % 2 == 0:
                result.append(p1[i//2])
            else:
                result.append(p2[i//2])
        return ''.join(result)
# transfer method
solve = Solution()
print(solve.reformat("covid2019"))