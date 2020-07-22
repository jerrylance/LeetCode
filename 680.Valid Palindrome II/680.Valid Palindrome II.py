# LeetCode Solution
# Zeyu Liu
# 2019.6.10
# 680.Valid Palindrome II

from typing import List
# method 1 two pointer,比较中间部分切片
class Solution:
    def validPalindrome(self, s: str) -> bool:
    	left = 0
    	right = len(s) - 1
    	while left < right:
    		if s[left] != s[right]:
    			one, two = s[left:right], s[left+1:right+1]
    			return one == one[::-1] or two == two[::-1]
    		left = left + 1
    		right = right -1
    	return True
# transfer method
solve = Solution()
print(solve.validPalindrome("addad"))

# method 2 方法1优化
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: 
        	return True
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n-1-i]:
                a = s[:i] + s[i+1:]
                b = s[:n-1-i] + s[n-i:]
                return a == a[::-1] or b == b[::-1]
        return True
# transfer method
solve = Solution()
print(solve.validPalindrome("addad"))