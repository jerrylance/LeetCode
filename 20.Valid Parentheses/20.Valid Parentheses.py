# LeetCode Solution
# Zeyu Liu
# 2019.2.24
# 20.Valid Parentheses

from typing import List
# method 1 stack栈的应用，pop()取出最后一个值并输出,重要，务必牢记，快
class Solution:
    def isValid(self, s: str) -> bool:
    	dic = {')':'(', ']':'[', '}':'{'}
    	stack = []
    	for i in s:
    		if i in dic.values():
    			stack.append(i)
    		elif i in dic.keys():
    			if stack == []:
    				return False
    			elif dic[i] != stack.pop():
    				return False
    	return stack == []
# transfer method
solve = Solution()
print(solve.isValid("([)]"))

# method 2 利用replace()，O(n2)，较慢
class Solution:
    def isValid(self, s: str) -> bool:
    	while '()' in s or '[]' in s or '{}' in s:
    		s = s.replace('()','').replace('[]','').replace('{}','')
    	return s == ''
# transfer method
solve = Solution()
print(solve.isValid("([)]"))