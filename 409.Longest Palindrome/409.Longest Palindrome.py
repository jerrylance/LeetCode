# LeetCode Solution
# Zeyu Liu
# 2019.3.16
# 409.Longest Palindrome

from typing import List
# method 1 计数法，奇偶数讨论，注意全偶数情况或全奇数情况flag
class Solution:
    def longestPalindrome(self, s: str) -> int:
        num = 0
        flag = 0
        for i in set(s):
            if s.count(i) % 2 == 0:
                num += s.count(i)
            else:
                num += s.count(i) - 1
                flag = 1
        return num + flag
# transfer method
solve = Solution()
print(solve.longestPalindrome("abccccdd"))

# method 2 字典法,stack思路
class Solution:
    def longestPalindrome(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i in stack:
                stack.remove(i)
                count += 2
            else:
                stack.append(i)
        if stack == []:
            return count
        return count + 1
# transfer method
solve = Solution()
print(solve.longestPalindrome("abccccdd"))