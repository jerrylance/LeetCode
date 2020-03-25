# LeetCode Solution
# Zeyu Liu
# 2019.3.10
# 344.Reverse String

from typing import List
# method 1 slice切片,较快
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
# transfer method
solve = Solution()
print(solve.reverseString(["H","a","n","n","a","h"]))

# method 2 排序
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
# transfer method
solve = Solution()
print(solve.reverseString(["H","a","n","n","a","h"]))

# method 3 reverse()
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
# transfer method
solve = Solution()
print(solve.reverseString(["H","a","n","n","a","h"]))