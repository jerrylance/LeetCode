# LeetCode Solution
# Zeyu Liu
# 2019.2.18
# 125.Valid Palindrome

from typing import List
# method 1 将符合要求的字符串形式存入，比较正反序是否一样, 较快
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                s1 += i.lower()
        return s1 == s1[::-1]

# transfer method
solve = Solution()
print(solve.isPalindrome("0P"))

# method 2 Two points, isalnum()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
        if not s[l].isalnum() and not s[r].isalnum():
            return True
        return s[l].lower() == s[r].lower()
# transfer method
solve = Solution()
print(solve.isPalindrome("aA"))