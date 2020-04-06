# LeetCode Solution
# Zeyu Liu
# 2019.3.19
# 434.Number of Segments in a String

from typing import List
# method 1 strip(),split()
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.strip().split())
        #return len(s.split())
# transfer method
solve = Solution()
print(solve.countSegments(", , , ,        a, eaefa"))

# method 2 遍历
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in s.split():
            count += 1
        return count
# transfer method
solve = Solution()
print(solve.countSegments(", , , ,        a, eaefa"))

# method 3 不用split()
class Solution:
    def countSegments(self, s: str) -> int:
        return sum(s[i] != ' ' and (i == 0 or s[i-1] == ' ') for i in range(len(s)))
# transfer method
solve = Solution()
print(solve.countSegments(", , , ,        a, eaefa"))