# LeetCode Solution
# Zeyu Liu
# 2019.3.18
# 459.Repeated Substring Pattern

from typing import List
# method 1 切片从大往小遍历,除法
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        c = 2
        d = len(s)
        while d > 1:
            if l % c == 0:
                d = l // c
                for i in range(c):
                    if s[d*i:d*(i+1)] == s[d*(i+1):d*(i+2)]:
                        if d*(i+2) == l:
                            return True
                    else:
                        break
                #if ''.join([s[:d]] * c) == s:
                #    return True
            c += 1
        return False
# transfer method
solve = Solution()
print(solve.repeatedSubstringPattern("abaabaa"))

# method 2 切片从小往大遍历
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(1, l // 2 + 1):
            if l % i == 0:
                d = l // i
                if ''.join([s[:i]] * d) == s:
                    return True
        return False
# transfer method
solve = Solution()
print(solve.repeatedSubstringPattern("abaabaa"))

# method 3 利用性质，两个s连起来去掉首尾,快
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sm = (s + s)[1:-1]
        if s in sm:
            return True
        return False
# transfer method
solve = Solution()
print(solve.repeatedSubstringPattern("abaabaa"))
