# LeetCode Solution
# Zeyu Liu
# 2019.3.17
# 392.Is Subsequence

from typing import List
# method 1 常规法，较快
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        i = 0
        for j in t:
            if j == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False
# transfer method
solve = Solution()
print(solve.isSubsequence("abc", "ahbgdc"))
# method 2 比对法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i >= m
# transfer method
solve = Solution()
print(solve.isSubsequence("abc", "ahbgdc"))

# method 3 iter()用法,迭代器,快
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(i in it for i in s)
# transfer method
solve = Solution()
print(solve.isSubsequence("abc", "ahbgdc"))

# method 4 find(),最快
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1
        for i in s:
            index = t.find(i, index+1)
            if index == -1:
                return False
        return True
# transfer method
solve = Solution()
print(solve.isSubsequence("abc", "ahbgdc"))

