# LeetCode Solution
# Zeyu Liu
# 2019.3.1
# 389.Find the Difference

from typing import List
# method 1 列表，暴力，慢
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l = list(t)
        for i in s:
            l.remove(i)
        return ''.join(l)
# transfer method
solve = Solution()
print(solve.findTheDifference("abcd", "abcde"))

# method 2 排序，找不同，较快
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(t)):
            try:
                if s[i] != t[i]:
                    return t[i]
            except:
                return t[-1]
# transfer method
solve = Solution()
print(solve.findTheDifference("a", "aa"))

# method 3 api,collections.Counter()记录出现次数,最快
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        import collections
        cs, ct = collections.Counter(s), collections.Counter(t)
        for key in ct.keys():
            if ct[key] - cs[key] == 1:
                return key
# transfer method
solve = Solution()
print(solve.findTheDifference("a", "aa"))