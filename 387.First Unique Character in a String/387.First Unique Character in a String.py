# LeetCode Solution
# Zeyu Liu
# 2019.3.12
# 387.First Unique Character in a String

from typing import List
# method 1 count,set,index,min, 快
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = []
        if s:
            for i in set(s):
                if s.count(i) == 1:
                    l.append(s.index(i))
            if l != []:
                return min(l)
        return -1
# transfer method
solve = Solution()
print(solve.firstUniqChar("loveleetcode"))

# method 2 Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        sc = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0)==1:
                return i
        return -1
# transfer method
solve = Solution()
print(solve.firstUniqChar("loveleetcode"))

# method 3 dict, 较慢
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for i in range(len(s)):
            c = s[i]
            if d[c]==1:
                return i
        return -1 
# transfer method
solve = Solution()
print(solve.firstUniqChar("loveleetcode"))